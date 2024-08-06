
# Variant 6
# ваніль інноватор
# 104235 234581067


word_to_crypt="Я__студент__НАУ__з__факультету_ФККПI__Деркач_Назарiй_!".upper()
print(len(word_to_crypt))
key_1 = "104235" 
key_2 = "234581067"
a=[]
s=-1
for x in range(len(word_to_crypt)):
        if x%len(key_2) == 0:
            a.append([])
            s+=1  
        a[s].append(word_to_crypt[x])

b = []
for x in range(len(a)):
        b.append([])
        for i in key_2:
            b[x].append(a[x][int(i)])

c=[]
for i in key_1:
      c.append(b[int(i)])

crypt_word = ""
for x in key_2:
        for i in c:
            crypt_word += i[int(x)]
print("\n")
print("Crypt word: ", crypt_word)
print("\n")