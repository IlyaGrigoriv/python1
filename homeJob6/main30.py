# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.

num,step,size = int(input()),int(input()),int(input())
list_1 = []
count = num
while size>0:
    list_1.append(count)
    size-=1
    count+=step
print(list_1) 
# for i in range(num,long+num,step ):
#     print(i)