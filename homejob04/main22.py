# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# from random import randint
# a = int(input('Ввидите кол-во элементов первого множества: '))
# b = int(input('Ввидите кол-во элементов второго множества: '))
from random import randint

n = 4#int(input("Ввидите число: "))
m = 5#int(input("Ввидите число: "))
list1 = {1}
list2 = {2}
# list1 = n,m
# print(list1)



def NewMany(list,n):

    for i in range(n):
        list.add(randint(1, 99))
    return list


list1 = NewMany(list1,n)
list2 = NewMany(list2,m)
print(list1)
print(list2)
# list3 = {}
list3 = list1.intersection(list2)
print(list3)

#работает
