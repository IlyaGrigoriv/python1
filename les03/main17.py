# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint
my_list = []
count_list =[]
for i in range(8):
    my_list.append(randint(-1,4)) 
    
print(*my_list) 
count_list = set(my_list)

print(len(count_list))   




# my_list = [2,3,5,7,4,3,5,3,2,45,6,3,12,5,7,4,5]
# new_set = set(my_list)
# new_list = list(set(my_list))
# new_tuple = tuple(set(my_list))
# cur_tuple = new_tuple[:-3]
# new_tuple = cur_tuple