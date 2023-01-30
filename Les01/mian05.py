# Найдите сумму цифр трехзначного числа.
num = 123  # int (input("В видите трехзначное число:  "))
num2 = num
i = 0
res = 0
count = 0
while num2 > 0:
    num2 = num2//10
    count+=1
    
    while i < count:
        res1 = num % 10
        # print(res1)
        res2 = num // 10
        # print(res2)
        num = res2
        res += res1
        i += 1
print(res)
