# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint
a,b = int(input()),int(input())
list_1 =[]
list_2 = []
for i in range (20):
    list_1.append(randint(-5,15))
print(list_1)    

for i in range(len(list_1)):
    if list_1[i] >= a and list_1[i] <= b:
        list_2.append(i)

print(list_2)