# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# #  Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# # Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# # для изменения и удаления данных.


# 1 импорт
# 2 экспорт
# 3 вывод данных
# 4 сохранять данные
# -10 пуск начало всей работы

#импорт
list_phoone = []
print(type(list_phoone))



def import_data (): #запись
    with open ('phooneboke.txt', 'a' , encoding= 'utf-8') as data:


#экспорт
def export_data (): #чтение
    with open ('phooneboke.txt', 'r' , encoding= 'utf-8') as data:
    for line in data:
        print(line)
        

def enter_print_data (data):
    data = input('Ввидите фамилию : ')
    data = input('Ввидите номер телефона : ')























# def expotr_data(): #записывает
#     with open ('phonebooke.txt', 'a+' , encoding= 'utf-8') as data:
#         data.writelines(''.join(new_contact) + '\n')
        
# def import_data(list): #читает
#     with open('phonebooke.txt', 'r' , encoding= 'utf-8') as data:
#         s = data.readlines()
#         for i in range(len(s)):
#             phonebook[i] = s [i].split() 

# def input_data(): 
#     new_contact = input('Ввидите новый контакт : ').split()

# expotr_data(new_contact)
    
# def plau_data(): 


 
    




#  -8 ввод.вывод данных пользовательский инткрфейс
#  -8 поиск даннных 

# def search_data():    


# input_data()
