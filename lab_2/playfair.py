# Playfair cipher with Ukrainian letters

# Define the alphabet
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя_,.'


def generate_matrix(key):
 
    key = ''.join(sorted(set(key), key=key.index))
    key_alphabet = key + alphabet
 
    matrix = [list(key_alphabet[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def encrypt(plaintext, key):
  
    matrix = generate_matrix(key)

    plaintext = plaintext.replace('й', 'і')
  
    plaintext_pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
   
    if len(plaintext) % 2 == 1:
        plaintext_pairs.append(plaintext[-1] + 'а')
  
    ciphertext_pairs = []
    for pair in plaintext_pairs:
       
        a, b = pair
        a_row, a_col = divmod(matrix.index([x for x in matrix if a in x][0]), 6)
        b_row, b_col = divmod(matrix.index([x for x in matrix if b in x][0]), 6)
      
        if a_row == b_row:
            a_col = (a_col + 1) % 6
            b_col = (b_col + 1) % 6
      
        elif a_col == b_col:
            a_row = (a_row + 1) % 6
            b_row = (b_row + 1) % 6
     
        else:
            a_col, b_col = b_col, a_col
   
        ciphertext_pairs.append(matrix[a_row][a_col] + matrix[b_row][b_col])

    ciphertext = ''.join(ciphertext_pairs)
    return ciphertext


def decrypt(ciphertext, key):
   
    matrix = generate_matrix(key)
  
    ciphertext_pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
  
    plaintext_pairs = []
    for pair in ciphertext_pairs:
       
        a, b = pair
        a_row, a_col = divmod(matrix.index([x for x in matrix if a in x][0]), 6)
        b_row, b_col = divmod(matrix.index([x for x in matrix if b in x][0]), 6)

    if a_row == b_row:
        a_col = (a_col - 1) % 6
        b_col = (b_col - 1) % 6
   
    elif a_col == b_col:
        a_row = (a_row - 1) % 6
        b_row = (b_row - 1) % 6

    else:
        a_col, b_col = b_col, a_col

        plaintext_pairs.append(matrix[a_row][a_col] + matrix[b_row][b_col])
   
        plaintext = ''.join(plaintext_pairs)

        plaintext = plaintext.replace('а', '')
   
        plaintext = plaintext.replace('і', 'й')
    return plaintext

plaintext = 'Я_студент_Богданович'
key = 'альтиметр'
ciphertext = encrypt(plaintext, key)
print(ciphertext) # output: 'яаарынввжєиэїїыыґві'

decrypted_plaintext = decrypt(ciphertext, key)
print(decrypted_plaintext) # output: 'моятаємнаінформація'