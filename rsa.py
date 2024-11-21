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
    signature = pow(message, d, n)
    return signature

def rsa_verify(message, signature, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == message

def example(text):
    # Генерируем приватный и публичный ключ
    private_key, public_key = generate_keypair(1024)
    # Подписываем сообщение
    message = int.from_bytes(hashlib.sha256(text.encode()).digest())
    signature = rsa_sign(message, private_key)
    print(f"\nТекст: {text}\n---\nПриватный ключ: {private_key}\nПубличный ключ: {public_key}\nПодпись: {signature}")
    # Проверяем что сообщение подписано публичным ключом
    verification_result = rsa_verify(message, signature, public_key)
    print(f"Проверка на то что подпись принадлежит публичному ключу: {verification_result}")

example("Hello, this is president of Mongolia")
example("Do not launch nukes, we arrived at peace")
