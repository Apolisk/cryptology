


plaintext = "З А Х И С Т І Н Ф О Р М А Ц І Ї"
values =["З","А","Х","И","С","Т","І","Н","Ф","О","Р","М","А","Ц","І","Ї"]

coordinates= [(0,0),(0,2),(2,1),(2,3),(0,1),(0,3),(2,0),(2,2),(1,0),(1,2),(3,1),(3,3),(1,1),(1,3),(3,0),(3,2)]

matrix = [['' for _ in range(4)] for _ in range(4)]  

for coord, value in zip(coordinates, values):
    x, y = coord
    matrix[x][y] = value
print("\n")
print("Створена матриця за допомогою координат: ")  
for i in matrix:
    print(i)

crypt_word=""

# for i in range(4):
#     for x in matrix:
#         print()
    

enc=""
for coord in coordinates:
    # print(coord)
    x, y = coord
    enc += matrix[x][y]
print("Розщифроване повiдомлення: ", enc)
print("\n")