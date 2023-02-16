# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Ввидите число: "))
m = int(input("Ввидите число: "))
list1 = []#[ i+1 for i in range(1,20) if i %2 ==0]
list2 = []#[ i+1 for i in range(1,20) if i %2 ==0]

def NewMany(list,n):

    for i in range(n):
        list.add(randint(1, 5))
    #print(list)
    return list


list1 = NewMany(list1,n)
list2 = NewMany(list2,m)
print(f'первый лист {list1}')
print(f'второй лист {list2}')
list3 = {0}
list3 = list1.intersection(list2)
print(f'итог {list3}')

#работает
