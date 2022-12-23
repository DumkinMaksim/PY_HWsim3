# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

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
print(numbers)


def num_sums(twonumb):
    sums=0
    for i in twonumb:
        sums+=i
    return sums
twonumb=numbers[1::2]
print(numbers[1::2])
print (num_sums(twonumb))