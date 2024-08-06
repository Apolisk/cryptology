list = [['А','Л','Ь','Т','И','М'],
        ['Е','Р','Б','В','Г','Ґ'],
        ['Д','Є','Ж','З','І','Ї'],
        ['Й','К','Н','О','П','С'],
        ['У','Ф','Х','Ц','Ч','Ш'],
        ['Щ','Ю','Я','_',',','.']]


plain_text = "Я_Студент_НАУ_"
plain_text = plain_text.upper()
text =''
for i in range(0, len(plain_text)):
    text += plain_text[i]
    if i % 2 != 0:
        text += ' '
text = text.split(' ')



for i in range(len(text)):
    for x in range(2):  
        for y in range(len(list)):
            for z in range(len(list[y])):
                if text[i][x] in list[z][y]:
                    print(list[z][y])

                    print(f"Finde: list [{z}][{y}]")
    print("-----------------------------------------------")
            




