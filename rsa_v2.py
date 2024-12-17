import random
import tkinter as tk
from tkinter import messagebox

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
        
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = (x * x) % n
            if x == n-1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        n |= 1  
        if is_prime(n):
            return n

def generate_keys(key_size=1024):
    p = generate_prime(key_size // 2)
    q = generate_prime(key_size // 2)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)

    public_key = (hex(e), hex(n))
    private_key = (hex(d), hex(n))

    return public_key, private_key

def sign_message(message, private_key):
    d = int(private_key[0], 16)
    n = int(private_key[1], 16)
    
    message_int = int.from_bytes(message.encode(), 'big')
    signature = pow(message_int, d, n)
    
    return hex(signature)

def verify_signature(message, signature, public_key):
    e = int(public_key[0], 16)
    n = int(public_key[1], 16)

    signature_int = int(signature, 16)
    message_int = int.from_bytes(message.encode(), 'big')
    decrypted_signature = pow(signature_int, e, n)
    
    return decrypted_signature == message_int

def generate_tk_keys():
    global public_key, private_key
    public_key, private_key = generate_keys()

    private_key_entry_d.delete(0, tk.END)
    private_key_entry_d.insert(tk.END, private_key[0]) 

    private_key_entry_n.delete(0, tk.END)
    private_key_entry_n.insert(tk.END, private_key[1]) 

    public_key_entry_e.delete(0, tk.END)
    public_key_entry_e.insert(tk.END, public_key[0])
    public_key_entry_n.delete(0, tk.END)
    public_key_entry_n.insert(tk.END, public_key[1])

    signature_entry.delete(0, tk.END)


def sign_tk_message():
    message = message_entry.get("1.0", tk.END)
    signature = sign_message(message, private_key)
    signature_entry.delete(0, tk.END)
    signature_entry.insert(tk.END, signature)

def verify_tk_signature():
    message = message_entry.get("1.0", tk.END)
    signature = signature_entry.get()

    public_key_e = public_key_entry_e.get()
    public_key_n = public_key_entry_n.get()

    result = verify_signature(message, signature, (public_key_e, public_key_n))

    if result:
        messagebox.showinfo("Верификация", "Подпись действительна")
    else:
        messagebox.showerror("Верификация", "Подпись не действительна")



root = tk.Tk()
root.title("RSA")

message_label = tk.Label(root, text="Текст:")
message_label.pack()
message_entry = tk.Text(root, height=10, width=40)
message_entry.pack()

private_key_label = tk.Label(root, text="Приватный ключ (d часть):")
private_key_label.pack()

private_key_entry_d = tk.Entry(root, width=40)
private_key_entry_d.pack()

private_key_label = tk.Label(root, text="Приватный ключ (n часть):")
private_key_label.pack()

private_key_entry_n = tk.Entry(root, width=40)
private_key_entry_n.pack()

private_key_button = tk.Button(root, text="Сгенерировать приватный ключ", command=generate_tk_keys)
private_key_button.pack()

public_key_label = tk.Label(root, text="Публичный ключ (e часть):")
public_key_label.pack()

public_key_entry_e = tk.Entry(root, width=40)
public_key_entry_e.pack()

public_key_label = tk.Label(root, text="Публичный ключ (n часть):")
public_key_label.pack()

public_key_entry_n = tk.Entry(root, width=40)
public_key_entry_n.pack()

signature_label = tk.Label(root, text="Подпись:")
signature_label.pack()
signature_entry = tk.Entry(root, width=40)
signature_entry.pack()

sign_button = tk.Button(root, text="Подписать текст", command=sign_tk_message)
sign_button.pack()

verify_button = tk.Button(root, text="Проверить подпись", command=verify_tk_signature)
verify_button.pack()

root.mainloop()
