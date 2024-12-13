import tkinter as tk
from tkinter import ttk, messagebox
import random

SBOX = (
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
    (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
    (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
    (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
    (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
    (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
    (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
)


def f(right, k_i):
    right = (right + k_i) & 0xFFFFFFFF
    right = s(right)
    output = ((right << 11) & 0xFFFFFFFF) | (right >> 21)
    return output


def s(right):
    return sum((SBOX[i][(right >> (4 * i)) & 0xf]) << (4 * i) for i in range(8))


def encryption_round(input_left, input_right, round_key):
    output_left, output_right = input_right, input_left ^ f(input_right, round_key)
    return output_left, output_right


def decryption_round(input_left, input_right, round_key):
    output_right, output_left = input_left, input_right ^ f(input_left, round_key)
    return output_left, output_right


def encrypt(block, key):
    left, right = block >> 32, block & 0xFFFFFFFF
    for i in range(32):
        k_i = key[i % 8] if i < 24 else key[7 - (i % 8)]
        left, right = encryption_round(left, right, k_i)
    return (left << 32) | right


def decrypt(block, key):
    left, right = block >> 32, block & 0xFFFFFFFF
    for i in range(32):
        k_i = key[i] if i < 8 else key[7 - (i % 8)]
        left, right = decryption_round(left, right, k_i)
    return (left << 32) | right

# Генерация ключей
def generate_key():
    key = [int.from_bytes(random.randbytes(4), 'little') for _ in range(8)]
    key_entry.delete(0, tk.END)
    key_entry.insert(0, ' '.join(hex(k)[2:].zfill(8) for k in key))
    return key

# Шифрование/дешифрование текста
def process_text(encrypt_mode):
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Ошибка", "Введите текст.")
        return

    try:
        key_str = key_entry.get()
        key = [int(k, 16) for k in key_str.split()]
        if len(key) != 8:
            messagebox.showerror("Ошибка", "Неправильный формат. Введите 8 байтов.")
            return

        if encrypt_mode:
            data = input_text.encode('utf-8')

            padding_length = 8 - (len(data) % 8)
            if padding_length != 8:
                data += bytes([padding_length] * padding_length)

            processed_data = b""
            for i in range(0, len(data), 8):
                block = int.from_bytes(data[i:i + 8], 'little')
                processed_block = encrypt(block, key)
                processed_data += processed_block.to_bytes(8, 'little')

            # Выводим как байты
            output_text = processed_data.hex()
        else:  
            try:
                data = bytes.fromhex(input_text)
            except ValueError:
                messagebox.showerror("Ошибка", "Неправильный байтовый формат для дешифрования.")
                return

            processed_data = b""
            for i in range(0, len(data), 8):
                block = int.from_bytes(data[i:i + 8], 'little')
                processed_block = decrypt(block, key)
                processed_data += processed_block.to_bytes(8, 'little')
            
            padding_value = processed_data[-1]
            if 1 <= padding_value <= 8:
                processed_data = processed_data[:-padding_value]

            output_text = processed_data.decode('utf-8', errors='ignore')


        output_text_box.delete("1.0", tk.END)
        output_text_box.insert("1.0", output_text)

    except ValueError:
        messagebox.showerror("Ошибка", "Формат: 8 чисел в байтовой форме.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Программа вызвала ошибку: {e}")


root = tk.Tk()
root.title("Алгоритм ГОСТ")

# Key Input
key_label = ttk.Label(root, text="Ключ (8 чисел в байтовом формате)")
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
