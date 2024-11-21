import string

# Функция шифрования
# Внутри функции происходит итерация по символам в тексте.
# Если символ является буквой, то проверяется, является ли он заглавной или строчной. 
# Затем символу присваивается новое значение, полученное путем сдвига его кода ASCII. 
# Если символ не является буквой, он остается без изменений. 
# Зашифрованный текст накапливается в переменной encrypted_text. В конце функция возвращает зашифрованный текст.
def encrypt(text, shift):
    encrypted_text = ""
    lang_char_count=26
    start_chars=['A', 'a']
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord(start_chars[0]) + shift) % lang_char_count + ord(start_chars[0]))
            else:
                encrypted_text += chr((ord(char) - ord(start_chars[1]) + shift) % lang_char_count + ord(start_chars[1]))
        else:
            encrypted_text += char
    return encrypted_text

# Функция принимает зашифрованный текст и сдвиг и возвращает дешифрованный текст. 
# Она вызывает функцию encrypt с отрицательным значением сдвига, чтобы выполнить обратное преобразование.
def decrypt(text, shift):
    return encrypt(text, -shift)

# Функция принимает зашифрованный текст и выполняет дешифрование методом частотного анализа. 
# letter_frequency - словарь, который содержит частоту появления каждой буквы в английском языке.
# Словарь заполнен данными из таблицы отсюда: https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_the_first_letters_of_a_word_in_English_language
# letter_count - словарь, который будет содержать количество каждой буквы в дешифрованном тексте
# Происходит итерация по всем возможным сдвигам от 0 до длины letter_frequency. 
# Для каждого сдвига выполняется дешифрование текста с помощью функции decrypt. 
# Затем подсчитывается количество каждой буквы в дешифрованном тексте и сохраняется в словаре
# В конце функция сортирует список decrypted_text_list 
# по разнице между частотой букв в дешифрованном тексте и ожидаемой частотой букв в английском языке.
def break_cipher(text):
    letter_frequency = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02,
                        'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11,
                        'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
                        'J': 0.10, 'Z': 0.07}
    letter_uppercase=string.ascii_uppercase 
    decrypted_text_list = []
    for shift in range(len(letter_frequency)):
        decrypted_text = decrypt(text, shift)
        letter_count = {letter: 0 for letter in letter_uppercase}
        for char in decrypted_text:
            if char.isalpha():
                letter_count[char.upper()] += 1
        decrypted_text_list.append((shift, decrypted_text, letter_count))
    decrypted_text_list.sort(key=lambda x: sum(abs(x[2].get(letter, 0) - letter_frequency[letter]) for letter in letter_frequency))
    return decrypted_text_list

# Функция для обработки примеров шифрования и дешифрования
def example(text, shift):
    print(f"\nТекст:  {text}\nСдвиг: {shift}\n---")

    encrypted_text = encrypt(text, shift)
    print(f"Зашифрованный текст: {encrypted_text}")

    decrypted_texts = break_cipher(encrypted_text)
    print("Дешифрование текста частотным анализом (от наиболее вероятного к наименее)\nСдвиг \tТекст")
    for decryption in decrypted_texts[0:5]:
        print(f"{decryption[0]} \t{decryption[1]}")

# Два примера
example("HELLO WORLD", 7)
example("GOLDEN TICKET TO WILLY WONKA FACTORY", 11)
