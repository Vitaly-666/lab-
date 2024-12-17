import random
import tkinter as tk
from tkinter import messagebox
import random

def check_for_prime(n, k=10):
    if n in (2, 3): return True
    if n < 2 or n % 2 == 0: return False

    d, r = n - 1, 0
    while d % 2 == 0:
        d, r = d // 2, r + 1

    def milrab_test(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    return all(milrab_test(random.randint(2, n - 2)) for _ in range(k))


def genprime(min_value, max_value):
    if min_value > max_value:
        raise ValueError("min_value должно быть меньше чем max_value")
    if min_value % 2 == 0:
        min_value += 1

    while True:
        candidate = random.randrange(min_value, max_value, 2)
        if check_for_prime(candidate):
            return candidate


def compgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calc_inv_mod(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def gen_keypair(prime1, prime2):
    product_n = prime1 * prime2
    phi = (prime1-1) * (prime2-1)
    exponent_e = random.randrange(1, phi)
    g = compgcd(exponent_e, phi)
    while g != 1:
        exponent_e = random.randrange(1, phi)
        g = compgcd(exponent_e, phi)
    exponent_d = calc_inv_mod(exponent_e, phi)
    return (exponent_e, product_n), (exponent_d, product_n)

def gen_sig(private_key, msg):
    exponent_e, modulus_n = private_key
    message_int = int.from_bytes(msg.encode(), 'big')
    signature_int = pow(message_int, exponent_e, modulus_n)
    return signature_int.to_bytes((signature_int.bit_length() + 7) // 8, 'big')

def check_sig(public_key, msg, signature):
    exponent_d, modulus_n = public_key
    signature_int = int.from_bytes(signature, 'big')
    message_int = pow(signature_int, exponent_d, modulus_n)
    return message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big') == msg.encode()


def generate_tk_keys():
    prime1 = genprime(2**127, 2**128)
    prime2 = genprime(2**127, 2**128)

    global public_key, private_key
    public_key, private_key = gen_keypair(prime1, prime2)

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
    signature = gen_sig(private_key, message)
    signature_entry.delete(0, tk.END)
    signature_entry.insert(tk.END, signature.hex())

def verify_tk_signature():
    message = message_entry.get("1.0", tk.END)
    signature = bytes.fromhex(signature_entry.get())

    public_key_e = int(public_key_entry_e.get())
    public_key_n = int(public_key_entry_n.get())

    result = check_sig((public_key_e, public_key_n), message, signature)

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
