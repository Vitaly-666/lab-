def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            
            # Сдвиг буквы
            shift = ord(key[key_index].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
            # Добавляем новую зашифрованную букву
            ciphertext += encrypted_char
            
            # Обновляем индекс ключа
            key_index = (key_index + 1) % len(key)
        else:
            # Символы вне алфавита не шифруются
            ciphertext += char
    
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            
            # Обратный сдвиг дешифровки
            shift = ord(key[key_index].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            
            plaintext += decrypted_char
            
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    
    return plaintext


def example(text, key):
    encrypted_text=encrypt(text, key)
    decrypted_text=decrypt(encrypted_text, key)
    print(f"\nТекст: {text}\nКлюч: {key}\n---\nЗашифрованный текст: {encrypted_text}\nДешифрованный текст: {decrypted_text}")

example("Attack immediately at dawn", "SECRETKEY")
example("Retreat troops", "HILDBEDD")
