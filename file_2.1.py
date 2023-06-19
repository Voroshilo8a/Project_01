# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(array):
    
    value = array[0]
    for item in array:
        
        if value > item:
            value = item
    
    return value

def maximum(array):
    
    value = array[0]
    for item in array:
        
        if value < item:
            value = item
    
    return value


# my_list = [4,6,2,1,9,63,-134,566]
my_list = [-52, 56, 30, 29, -54, 0, -110]
# my_list = [42, 54, 65, 87, 0]
# my_list = [5]

print(f"min = {minimum(my_list)}, max = {maximum(my_list)}")