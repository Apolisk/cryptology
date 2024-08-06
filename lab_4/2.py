# Variant 6
# гречка

def crypt(word_to_crypt):
    key = "142530"
    word_to_crypt=word_to_crypt.upper()
    crypt_word = ""
    a = []
    s = -1
    # create matrix
    for x in range(len(word_to_crypt)):
        if x%len(key) == 0:
            a.append([])
            s+=1  
        a[s].append(word_to_crypt[x])
    print(a)
    # crypt algoritm
    for x in key:
        for i in a:
            crypt_word += i[int(x)]

    return crypt_word
print("\n")
print(crypt(word_to_crypt="Я_студент_НАУ_Деркач___!"))

print("\n")