# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint
size = int(input("Ввидите длинну массива: "))

my_list = []

for i in range(size):
    my_list.append(randint(0, 10))
print(my_list)

x = my_list[size-1]
a = x-1
b = x+1
print(x)
countX = 0
numX =0
for i in range(size):
    if my_list[i] == a or my_list[i] == b:
        numX = my_list[i]
        countX +=1

print(f'Ближайшее искоме число {numX} к нашему искомому число {x} встречается {countX} раз ')
#работает
