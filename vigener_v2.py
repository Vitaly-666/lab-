from collections import Counter
import string
import tkinter as tk
from tkinter import scrolledtext


def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    ciphertext = ""
    key_length = len(key)
    
    for i in range(len(plaintext)):
        # Конвертируем буквы в цифры (A=0, B=1)
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i % key_length]) - ord('A')
        # Используем формулу Вижинереа и конверируем обратно в букву
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))
    
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        # Конвертирование букв в цифр
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i % key_length]) - ord('A')
        # Обратно в буквы
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))
    
    return plaintext

# Частотный анализ 
def get_frequency_score(text):

    letter_frequences =  {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02,
                        'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11,
                        'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
                        'J': 0.10, 'Z': 0.07}

    freq = Counter(text)
    text_len = len(text)
    
    if text_len == 0:
        return float('inf')
    
    score = 0
    for letter in string.ascii_uppercase:
        observed_freq = freq[letter] / text_len
        expected_freq = letter_frequences[letter]
        score += abs(observed_freq - expected_freq)
    
    return score

# Попытка взлома шифра с помощью частного анализа и размеру ключа = key_length
def break_cipher(ciphertext, key_length):
    # Разбиваем текст на группы, которые были зашифрованы одной и той же буквой ключа

    groups = [''] * key_length
    for i in range(len(ciphertext)):
        groups[i % key_length] += ciphertext[i]
    
    #Находим наиболее вероятную букву ключа для каждой позиции
    key = ''
    for group in groups:
        best_shift = 0
        best_group_score = float('inf')
        
        # Перебираем все возможные сдвиги для этой позиции
        for shift in range(1,26):
            # Расшифрока группы с этим сдвигом
            decoded = ''.join(chr((ord(c) - ord('A') - shift) % 26 + ord('A')) for c in group)
            score = get_frequency_score(decoded)
            
            if score < best_group_score:
                best_group_score = score
                best_shift = shift
        
        key += chr(best_shift + ord('A'))
    
    return key

 # Функция для обработки шифровки/дешифровки
def process_text():
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get()

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)
    # broken = break_cipher(encrypted, 5)

    encrypted_output.delete("1.0", tk.END)
    decrypted_output.delete("1.0", tk.END)
    broken_output.delete("1.0", tk.END)

    encrypted_output.insert(tk.END, encrypted)
    decrypted_output.insert(tk.END, decrypted)

    broken_output.insert(tk.END, "Ключ | Дешифрованный текст\n")
    broken_output.insert(tk.END, "-" * 40 + "\n")

    for key_length in range(1, 10):
        key = break_cipher(encrypted, key_length)
        broken_output.insert(tk.END, f"{key:7} | {decrypt(encrypted, key)}\n")


# Cоздание основного окна
root = tk.Tk()
root.title("Шифт Виженера")

# Поля ввода
tk.Label(root, text="Текст ввода:").pack()
text_input = scrolledtext.ScrolledText(root, width=50, height=10)
text_input.pack()

tk.Label(root, text="Ключ:").pack()
key_input = tk.Entry(root)
key_input.pack()

# Кнопки
process_button = tk.Button(root, text="Обработать", command=process_text)
process_button.pack()

# Поля вывода
tk.Label(root, text="Зашифрованный текст:").pack()
encrypted_output = scrolledtext.ScrolledText(root, width=50, height=10)
encrypted_output.pack()

tk.Label(root, text="Дешифрованный текст:").pack()
decrypted_output = scrolledtext.ScrolledText(root, width=50, height=10)
decrypted_output.pack()

tk.Label(root, text="Самые возможные варианты частотного анализа:").pack()
broken_output = scrolledtext.ScrolledText(root, width=50, height=10)
broken_output.pack()

root.mainloop()
