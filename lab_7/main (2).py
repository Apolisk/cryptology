from Crypto.Cipher import DES
from Crypto.Random import random

# Функція для генерації ключа за алгоритмом BBS
def generate_key():
    p = 32416189867  # Велике просте число p
    q = 18264125061  # Велике просте число q

    n = p * q
    s = random.randint(0, n)  # Секретне значення s

    key = ''
    for _ in range(64):
        s = (s * s) % n  # Обчислення s^2 mod n
        bit = s % 2  # Отримання найменшого біта s
        key += str(bit)

    return key


# Реалізація блоку Фейстеля
def feistel_block(data, key):
    l = data[:4]
    r = data[4:]

    for i in range(16):
        temp = r
        r = str(int(l) ^ int(r) ^ int(key[i]))
        l = temp

    return r + l

    
# Функція для шифрування тексту
def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


# Функція для дешифрування тексту
def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# Отримання перших 64 біт гами "прізвищеім'я"
plaintext = 'Компанець Данило'.encode()[:8]

# Генерація ключа
key = generate_key()
key = int(key, 2).to_bytes(8, byteorder='big')

# Шифрування
ciphertext = encrypt(plaintext, key)

# Дешифрування
decrypted_text = decrypt(ciphertext, key).decode()

# Виведення результатів
print('Відкритий текст:', plaintext.decode())
print('Зашифрований текст:', ciphertext)
print('Дешифрований текст:', decrypted_text)
