# ; Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# ; разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# ; стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# ; гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# ; слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# ; от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# ; напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# ; в порядке
# from random import randint
# list_1 = [randint(1,50) for x in range(1,10) ]
# print(list_1)
my_list = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

#my_list = tuple(my_list)
flag = False
print(my_list)
count = 0
# num = [0]
k = 0
for i in my_list:
    
    if i == 'а':
        count+=1
        # num.append(count)
    if i == ' ':
        if sum == count and sum != 0:
            flag = True
        else:
            flag = False
        sum = count 
        count =  0
        # num.append(count)

# num.append(0)        
# print(num)

if flag ==True:
    print('Парам пам-пам')
else:
    print('NO')                    


        
        

