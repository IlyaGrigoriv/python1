# 1 экспотр данных
# 1 импорт данных

def expotr_data(): #записывает
    with open ('phonebooke.txt', 'a+' , encoding= 'utf-8') as data:
        data.writelines(''.join(new_contact) + '\n')
        
def import_data(): #читает
    with open('phonebooke.txt', 'r' , encoding= 'utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s [i].split() 
