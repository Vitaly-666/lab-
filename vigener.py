import tkinter as tk
from tkinter import messagebox

def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    
    return plaintext

def perform_action():
    text = text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    
    if not key:
        messagebox.showerror("Ошибка", "Ключ не может быть пустым.")
        return
    
    if action_var.get() == "Зашифровать":
        result = encrypt(text, key)
    else:
        result = decrypt(text, key)
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# Основное окно
root = tk.Tk()
root.title("Шифр Виженера")

tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=5)

tk.Label(root, text="Enter Key:").pack(pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.pack(pady=5)

action_var = tk.StringVar(value="Зашифровать")
tk.Radiobutton(root, text="Зашифровать", variable=action_var, value="Зашифровать").pack(anchor=tk.W)
tk.Radiobutton(root, text="Дешифровать", variable=action_var, value="Дешифровать").pack(anchor=tk.W)

tk.Button(root, text="Выполнить команду", command=perform_action).pack(pady=10)

tk.Label(root, text="Итог:").pack(pady=5)
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

root.mainloop()

