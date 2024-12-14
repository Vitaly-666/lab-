import tkinter as tk
from tkinter import ttk, messagebox

# S-блоки 
SBOX = [
    [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
    [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
    [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
    [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
    [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
    [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
    [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
    [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12],
]

#  Генерация подключей из основного ключа
def generate_subkeys(key):
    subkeys = []
    for i in range(0, len(key), 4):
        subkeys.append(int.from_bytes(key[i:i+4], 'little'))
    return subkeys

# Функция подстановки с использованием S-блоков
def substitute(value):
    result = 0
    for i in range(8):
        result |= ((SBOX[i][(value >> (4 * i)) & 0xF]) << (4 * i))
    return result

# Функция для одного раунда/этапа шифрования
def round_function(block, subkey):
    temp = (block + subkey) & 0xFFFFFFFF
    temp = substitute(temp)
    return ((temp << 11) | (temp >> (32 - 11))) & 0xFFFFFFFF

# Шифрование одного блока
def encrypt_block(block, subkeys):
    left = block & 0xFFFFFFFF
    right = block >> 32
    
    for i in range(32):
        key_index = i % 8
        temp = left
        left = right
        right = temp ^ round_function(right, subkeys[key_index])
    
    return (left << 32) | right

# Дешифровка одного блока
def decrypt_block(block, subkeys):
    left = block & 0xFFFFFFFF
    right = block >> 32
    
    for i in range(32):
        key_index = (31 - i) % 8
        temp = left
        left = right
        right = temp ^ round_function(right, subkeys[key_index])
    
    return (left << 32) | right

# Дополнение сообщения до кратности 8 байт
def pad_message(message):
    padding_length = 8 - (len(message) % 8)
    if padding_length == 8:
        padding_length = 0
    return message + bytes([padding_length] * padding_length)

# Удаление дополнения из сообщения
def unpad_message(padded_message):
    padding_length = padded_message[-1]
    if padding_length == 0:
        return padded_message
    return padded_message[:-padding_length]

# Шифрование сообщения
def encrypt(message, key):
    subkeys = generate_subkeys(key)
    message_bytes = message.encode('utf-8')
    padded = pad_message(message_bytes)
    
    result = bytearray()
    for i in range(0, len(padded), 8):
        block = int.from_bytes(padded[i:i+8], 'little')
        encrypted_block = encrypt_block(block, subkeys)
        result.extend(encrypted_block.to_bytes(8, 'little'))
    
    return bytes(result)

# Расшифрование сообщения
def decrypt(encrypted_message, key):
    subkeys = generate_subkeys(key)
    
    result = bytearray()
    for i in range(0, len(encrypted_message), 8):
        block = int.from_bytes(encrypted_message[i:i+8], 'little')
        decrypted_block = decrypt_block(block, subkeys)
        result.extend(decrypted_block.to_bytes(8, 'little'))
    
    unpadded = unpad_message(bytes(result))
    return unpadded.decode('utf-8')

def generate_key():
    import os
    key = os.urandom(32)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.hex())
    return key

# Шифрование/дешифрование текста
def process_text(encrypt_mode):
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Ошибка", "Введите текст.")
        return

    try:
        key = bytes.fromhex(key_entry.get())

        if encrypt_mode:
            data = input_text
            
            processed_data = encrypt(data, key)

            # Выводим как байты
            output_text = processed_data.hex()
        else:  
            try:
                data = bytes.fromhex(input_text)
            except ValueError:
                messagebox.showerror("Ошибка", "Неправильный байтовый формат для дешифрования.")
                return

            processed_data = decrypt(data, key)

            output_text = processed_data


        output_text_box.delete("1.0", tk.END)
        output_text_box.insert("1.0", output_text)

    except ValueError:
        messagebox.showerror("Ошибка", "Нажмите кнопку сгенерировать ключ")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Программа вызвала ошибку: {e}")


root = tk.Tk()
root.title("Алгоритм ГОСТ")

key_label = ttk.Label(root, text="Ключ")
key_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
key_entry = ttk.Entry(root, width=50)
key_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Кнопка генерации ключей
generate_key_button = ttk.Button(root, text="Сгенерировать ключ", command=generate_key)
generate_key_button.grid(row=0, column=2, padx=5, pady=5)

# Ввод
input_label = ttk.Label(root, text="Текст на вход:")
input_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
input_text_box = tk.Text(root, height=5, width=60)
input_text_box.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

# Кнопка шифрования
encrypt_button = ttk.Button(root, text="Зашифровать", command=lambda: process_text(True))
encrypt_button.grid(row=2,column=0, columnspan=3, padx=5, pady=10, sticky=tk.EW)

# Кнопка дешифрования
decrypt_button = ttk.Button(root, text="Дешифровать", command=lambda: process_text(False))
decrypt_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky=tk.EW)

# Вывод
output_label = ttk.Label(root, text="Итог:")
output_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
output_text_box = tk.Text(root, height=5, width=60)
output_text_box.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)


root.mainloop()
