# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

numbs=[4.07, 5.1, 8.2444, 6.98]
print('Даны элементы', numbs)

temp_list=[]
for i in numbs:
    temp_list.append(str(str(i).split('.')[1]))

print('Дробная часть элементов списка',temp_list)

def find_min_max(numb_list):
    rez_minmax=0
    max_numb=max(numb_list)
    min_numb=min(numb_list)
    print('Max-> '+str(max_numb)+'   Min-> '+str(min_numb))
   
    if int(max_numb)<10:
        max_numb=int(max_numb)*10
    rez_minmax=int(max_numb)-int(min_numb)
       
    
    return 'Разница между максимальным и минимальным значением дробной части элементов-> '+str(rez_minmax)

print(find_min_max(temp_list))