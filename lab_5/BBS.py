def blum_blum_shub(seed, string):
    length = len(string)
    p = 7879
    q = 7907
    n = p * q
    x = seed % n
    res = ''
    result = ''

    for i in range(length):
        for j in range(8):
            x = (x * x) % n
            bit = x % 2
            res += str(bit)
            
        if i == length - 1:
            result += res
            res = ''
        else:
            result += res
            res = ''
    
    return result
# dvikove gamuvany
def encrypt(keystream, plaintext):
    ciphertext = ''
    for i in range(len(plaintext)):
        # operazia XOR
        # ord  UNICODE 
        encrypted_char_code = ord(plaintext[i]) ^ int(keystream[i], 2)
        ciphertext += chr(encrypted_char_code)
        
    return ciphertext

def decrypt(keystream, ciphertext):
    plaintext = ''
    for i in range(len(ciphertext)):
        # operazia XOR
        # ord ord  UNICODE 
        decrypted_char_code = ord(ciphertext[i]) ^ int(keystream[i], 2)
    
        plaintext += chr(decrypted_char_code)
        
    return plaintext
key = 1234
plaintext = 'Hello, world!'
keystream = blum_blum_shub(key, plaintext).split(' ')
encrypted_text = encrypt(keystream, plaintext)
print('Encrypted text:', encrypted_text)
decrypted_text = decrypt(keystream, encrypted_text)
print('Decrypted text:', decrypted_text)
