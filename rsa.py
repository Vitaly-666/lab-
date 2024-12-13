import tkinter as tk
from tkinter import messagebox
import random
import hashlib

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1
        if is_prime(p):
            return p

def generate_keypair(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def rsa_sign(message, private_key):
    d, n = private_key
    signature = pow(hash_message(message), d, n)
    return signature

def rsa_verify(message, signature, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == hash_message(message)

def hash_message(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

def generate_private_key():
    global public_key
    public_key, private_key = generate_keypair(1024)
    private_key_bytes = private_key_to_bytes(private_key)
    public_key_bytes = public_key_to_bytes(public_key)
    private_key_entry.delete(0, tk.END)
    private_key_entry.insert(tk.END, private_key_bytes.hex())
    public_key_entry.delete(0, tk.END)
    public_key_entry.insert(tk.END, public_key_bytes.hex())

def private_key_to_bytes(private_key):
    d, n = private_key
    return d.to_bytes(128, 'big') + n.to_bytes(128, 'big')

def public_key_to_bytes(public_key):
    e, n = public_key
    return e.to_bytes(128, 'big') + n.to_bytes(128, 'big')

def sign_message():
    message = message_entry.get("1.0", tk.END)
    private_key_bytes = bytes.fromhex(private_key_entry.get())
    private_key = bytes_to_private_key(private_key_bytes)
    signature = rsa_sign(message, private_key)
    signature_bytes = signature.to_bytes(128, 'big')
    signature_entry.delete(0, tk.END)
    signature_entry.insert(tk.END, signature_bytes.hex())

def verify_signature():
    message = message_entry.get("1.0", tk.END)
    signature_bytes = bytes.fromhex(signature_entry.get())
    signature = int.from_bytes(signature_bytes, 'big')
    public_key_bytes = bytes.fromhex(public_key_entry.get())
    public_key = bytes_to_public_key(public_key_bytes)
    result = rsa_verify(message, signature, public_key)
    if result:
        messagebox.showinfo("Верификация", "Подпись действительна")
    else:
        messagebox.showerror("Верификация", "Подпись не действительна")

def bytes_to_private_key(private_key_bytes):
    d = int.from_bytes(private_key_bytes[:128], 'big')
    n = int.from_bytes(private_key_bytes[128:], 'big')
    return (d, n)

def bytes_to_public_key(public_key_bytes):
    e = int.from_bytes(public_key_bytes[:128], 'big')
    n = int.from_bytes(public_key_bytes[128:], 'big')
    return (e, n)

root = tk.Tk()
root.title("RSA")

message_label = tk.Label(root, text="Текст:")
message_label.pack()
message_entry = tk.Text(root, height=10, width=40)
message_entry.pack()

private_key_label = tk.Label(root, text="Приватный ключ:")
private_key_label.pack()
private_key_entry = tk.Entry(root, width=40)
private_key_entry.pack()
private_key_button = tk.Button(root, text="Сгенерировать приватный ключ", command=generate_private_key)
private_key_button.pack()

public_key_label = tk.Label(root, text="Публичный ключ:")
public_key_label.pack()
public_key_entry = tk.Entry(root, width=40)
public_key_entry.pack()

signature_label = tk.Label(root, text="Подпись:")
signature_label.pack()
signature_entry = tk.Entry(root, width=40)
signature_entry.pack()

sign_button = tk.Button(root, text="Подписать текст", command=sign_message)
sign_button.pack()

verify_button = tk.Button(root, text="Проверить подпись", command=verify_signature)
verify_button.pack()

root.mainloop()
