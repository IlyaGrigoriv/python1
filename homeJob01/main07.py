# # # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# # # расплачивались за проезд и получали билет с номером. Счастливым
# # # билетом называют такой билет с шестизначным номером, где сумма
# # # первых трех цифр равна сумме последних трех. Т.е. билет с номером
# # # 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# # # программу, которая проверяет счастливость билета.
# # примеры
# # 385916 -> yes
# # 123456 -> no

num = 385916  # int (input('В видите число: '))
num1 = num
num2 = num // 1000
res1 = 0
res2 = 0
for i in range(3):
    res1 += num1 % 10
    num1 = num1//10
num2 = num // 1000

for i in range(3):
    res2 += num2 % 10
    num2 = num2//10
if res1 == res2:
    print('yes')
else:
    print('no')

# print(res1)
# print(res2)

# print (123//2)
