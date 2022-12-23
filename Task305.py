
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

 
n = int(input('Enter N-> '))
 
def fibanacci(n):
    one_num,two_num=1,1
    for i in range(n):
        yield one_num
        one_num,two_num=two_num,one_num+two_num
fibadata=list(fibanacci(n))
print(fibadata)


def negafibanacci(n):
    one_num,two_num=0,1
    for i in range(n+1):
        yield one_num
        one_num,two_num=two_num,one_num-two_num
fibadata=list(fibanacci(n))
negfibadata=list(negafibanacci(n))
negfibadata=negfibadata[::-1]
print(negfibadata+fibadata)

