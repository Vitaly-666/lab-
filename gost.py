from random import randbytes

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

key = [0xFFFFFFFF, 0x12345678, 0x00120477, 0x77AE441F, 0x81C63123, 0x99DEEEEE, 0x09502978, 0x68FA3105]

def example(text, key):
    encrypted_text=encrypt(int.from_bytes(text.encode("utf-8")), key)
    decrypted_text=decrypt(encrypted_text, key)
    print(f"\nТекст: {text}\nКлюч: {key}\n---\nЗашифрованный текст: {hex(encrypted_text)}\nДешифрованный текст: {decrypted_text.to_bytes(((decrypted_text.bit_length() + 7) // 8), byteorder='big').decode('utf-8')}")

example("Hello beautiful world!", [int.from_bytes(randbytes(8)) for i in range(8)])
example("I have a dream", [int.from_bytes(randbytes(8)) for i in range(8)])
