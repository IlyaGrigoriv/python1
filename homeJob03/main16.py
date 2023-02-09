# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
from random import randint
size = int(input("Ввидите длинну массива: "))

my_list = []

for i in range(size):
    my_list.append(randint(0,10))
print (my_list)    

x = my_list[size-1]
print (x)
countX = 0
for i in range(size):
    if my_list[i] == x:
        countX +=1
print(f'Число {x} встречается в массиве {countX} раз')        
#работает