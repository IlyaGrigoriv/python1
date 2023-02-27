#  -8 ввод.вывод данных пользовательский инткрфейс
#  -8 поиск даннных 

# 1 новый контакт
# 2 создать контакт
# 3 поиск контакта
# 4 удаление контакта   
    
list_phone = []

def new_contact(list_phone):
    list_phone.append(input('Ввидите ФИО :  '))
    list_phone.append(input('Ввидите телефон :  '))


def search_contact(list_phone):
    search = input('Ввидите имя или телефон:  ')
    for i in list_phone:
        if i == search:
            print (i)


def del_contact(list_phone):
    search = input('Ввидите имя или телефон:  ')
    for i in list_phone:
        if i == search:
            i = ' '




