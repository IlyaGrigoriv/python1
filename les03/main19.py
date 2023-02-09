# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
k = int(input('Ввидите число: '))
my_list = []
count_list =[]
for i in range(5):
    my_list.append(randint(1,6)) 
print(my_list)

