
alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ.,_!"

vid_shifruvanya = int(input("Цезаря - 1 Лінійний - 2 Афінний- 3\n Оберiть шифр: "))
match vid_shifruvanya:
    case 1:
        method = int(input("Шифрування - 1\t Дешифрування - 2 \n Оберiть метод: " ))
        key = int(input("Введiть ключ: "))
        word =  input("ВВедiть слово: ")
        word = word.upper()
        match method:
            case 1:
                crypt_word = ''
                for i in word:
                    letter_index = alphabet.find(i)
                    new_index = (letter_index + key)%len(alphabet)
                    crypt_word += alphabet[new_index]
                print(crypt_word)
            case 2:
                encrypt_word = ''
                for i in word:
                    letter_index = alphabet.find(i)
                   
                    new_index = (letter_index +len(alphabet)-key)%len(alphabet)
                    encrypt_word += alphabet[new_index]
                print(encrypt_word)
    case 2:
        method = int(input("Шифрування - 1\t Дешифрування - 2 \n Оберiть метод: " ))
        key = int(input("Введiть ключ: "))
        word =  input("ВВедiть слово: ")
        word = word.upper()
        match method:
            case 1:
                crypt_word = ''
                for i in word:
                    letter_index = alphabet.find(i)
                    new_index = letter_index * key % len(alphabet)
                    crypt_word += alphabet[new_index]
                print(crypt_word)
            case 2:
                fi_m =len(alphabet)-1
                eyler_key = key**(fi_m-1)%len(alphabet)
                print(eyler_key)           
                encrypt_wrod = ''
                for i in word:
                    letter_index = alphabet.find(i)
                    # print("Letter_index: ", letter_index)
                    new_index = letter_index*eyler_key%len(alphabet)
                    # print("New_index: ", new_index) 
                    encrypt_wrod += alphabet[new_index]
                print(encrypt_wrod)
    case 3:
        method = int(input("Шифрування - 1\t Дешифрування - 2 \n Оберiть метод: " ))
        key_k= int(input("Введiть ключ k: "))
        key_t = int(input("Введiть ключ t: "))
        word =  input("ВВедiть слово: ")
        word = word.upper()
        # Обов’язковою умовою реалізації даного шифру є те,
        # що кількість символів відкритого тексту повинно бути простим
        # числом.
        if len(word) % 2 ==0:

            print("Кількість символів відкритого тексту не просте число")
        else: 
            match method:
                case 1:
                    crypt_word = ''
                    for i in word:
                        letter_index = alphabet.find(i)
                        new_index = (letter_index*key_k+key_t)%len(alphabet)
                        print(f"{new_index}")
                        crypt_word += alphabet[new_index]
                    print(crypt_word)
                case 2:
                    encrypt_word = ''
                    for i in word:
                        index = alphabet.find(i)
                        fi_m =len(alphabet)-1
                        k_ = key_k**(fi_m-1)%len(alphabet) 
                     
                        t_ =  -k_*key_t%len(alphabet)
                        print(k_, t_)
                        new_index = (index*k_+t_)%len(alphabet)
                        encrypt_word += alphabet[new_index]
                    print(encrypt_word)