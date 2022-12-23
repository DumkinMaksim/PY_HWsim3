# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

number_of_elements=int(input("Enter number of elements-> "))
def rand_nums(num_min:int,num_max:int, kolvo:int): 
    '''
    функция генерирует рандомные целые цисла 
    принимает целые 
    num_min-минимальное знацение
    num_max- максимальное значение диапазона
    kolvo- количество элементов
    на выходе список целых чисел из указанных входных данных
    '''
    for i in range(kolvo):
        randa_num=[ random.randint(num_min, num_max) for i in range(kolvo)]
        return randa_num

numbers=rand_nums(-20,20,number_of_elements)
one_list=numbers
print(one_list)


def find_mult_elements(оne_list):
    '''
    Принимает список целых чисел и находит произведение крайних элементов
    '''
    if len(one_list)%2==0:
        minisize=len(one_list)/2
    else:
        minisize=int((len(one_list)/2)+0.5)
    rezult_list=[]
    i=0

    while i<=minisize-1:
        rezult_list.append(one_list[i]*one_list[(i+1)*-1])
        i+=1
    
    return rezult_list

print(find_mult_elements(one_list))