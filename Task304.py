# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

binary=[]
def find_decimal_to_binary(number,m):
    '''
    решение с использованием рекурсии
    '''
    if number==0:
        return 1
    else:
        binary.insert(m,number%2)    
    return find_decimal_to_binary(number//2,m-1)
num=find_decimal_to_binary(int(input('Введите десятичное число-> ')),-1)
print(binary)

