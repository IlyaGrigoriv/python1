# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

n = int(input('Ввидите число: '))


def NumFibonachi(num):
    i = 0
    j = 1
    k = 1
    while i <= num:  # 1,1,2,3,5
        k = i+j

        if i == num:
            print(i)
        elif i > num:
            print("-1")
    return (i)

numFibonachi=NumFibonachi(n)
print(numFibonachi)