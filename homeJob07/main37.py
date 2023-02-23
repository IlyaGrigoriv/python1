# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения
num_rows = 6 #int(input())
num_colums = 6 #int(input())


# [[my_func(i) for i in range(7)] for _ in range(4)]
my_list = []
my_list = [[ (column+1)*(row+1) for column in range(num_colums)] for row in range(num_rows)]
print(my_list)
# operanion = lambda i,j : i*j
# print_operation_table = list(map(operanion,my_list))

