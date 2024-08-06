
word_to_crypt = "абонент"
# Ключ згiдно варiанту №6
3572641 
key = "2461530"

crypted_word = ""

encrypted_word =""

for i in key:
    crypted_word+=word_to_crypt[int(i)]
print("Зашифроване слово: ", crypted_word)

for i in range(len(word_to_crypt)):
    encrypted_word+=word_to_crypt[int(i)]
print("Розшифроване слово: ",encrypted_word)
