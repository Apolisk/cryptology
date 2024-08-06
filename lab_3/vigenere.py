

alphabets = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ " 
alphabets = alphabets.lower()
def encrypt(p, k):
    c = ""
    kpos = [] 
    for x in k:
       
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i] 
      
      if pos > 32:
          pos = pos-33             
      c += alphabets[pos].capitalize()  
      i +=1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 33
      p += alphabets[pos].lower()
      i +=1
    return p
try:
    print("Введiть 1 для шифрування 2- для дешифрування")
    choose = input("Оберiть: ")
    if choose == '1':
       p = input("введiть текст: ")
       p = p.replace(" ", "")  
       if p.isalpha():
           k = input("введiть ключ: ")
           k = k.strip()  
           if k.isalpha():

               c = encrypt(p, k)
               print("шфрованый текст: ", c)

           else:
               print(k)
               print("Enter valid key")
       else:
           print("only letters are allowed !!")

    elif choose == '2':
        c = input("введiть зашифрований текст: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("введiть ключ: ")
            if not k.isalpha():
                print("Enter valid key")
            else:
                p = decrypt(c, k)
                print("розширований текст: ", p)
        else:
            print("only letters are allowed!")

    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")
