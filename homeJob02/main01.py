# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:0.

# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Ввидите число: '))
if type(n) == float:
    # print(f'1\{n}')
    for i in range(2):# незнаю как правильно сделать универсальный щетчик
        n = n*10
        i += 1
        # print(f'2\{n}')
res = 0

while n != 0:
    res += n % 10
    n = n//10

print(round(res))
# работает
