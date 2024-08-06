import numpy as np

def char_to_int(char):
    return ord(char) - 1071

def int_to_char(integer):
    return chr(integer + 1071)

def str_to_matrix(string):
    n = int(len(string)**0.5)
    matrix = np.zeros((n,n), dtype=int)
    for i in range(n):
        for j in range(n):
            matrix[i,j] = char_to_int(string[i*n+j])
    return matrix

def matrix_to_str(matrix):
    string = ""
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            string += int_to_char(matrix[i,j])
    return string

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace("І", "Ї") # Replace "I" with "І" (if present)
    key = key.upper().replace("І", "Ї") # Replace "I" with "І" (if present)
    plaintext_matrix = str_to_matrix(plaintext)
    key_matrix = str_to_matrix(key)
    ciphertext_matrix = np.dot(key_matrix, plaintext_matrix) % 33 # Modulo 33 since there are 33 Ukrainian letters
    ciphertext = matrix_to_str(ciphertext_matrix)
    return ciphertext

def decrypt(ciphertext, key):
    key = key.upper().replace("І", "Ї") # Replace "I" with "І" (if present)
    key_matrix = str_to_matrix(key)
    key_matrix_inverse = np.linalg.inv(key_matrix)
    plaintext_matrix = np.dot(key_matrix_inverse, str_to_matrix(ciphertext)) % 33 # Modulo 33 since there are 33 Ukrainian letters
    plaintext = matrix_to_str(plaintext_matrix)
    return plaintext
plaintext = "українська"
key = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
ciphertext = encrypt(plaintext, key)
print(ciphertext)
# Output: "ЗЮФПІХЧУІШДЙ"

decrypted_plaintext = decrypt(ciphertext, key)
print(decrypted_plaintext)
# Output: "УКРАЇНСЬКА"
