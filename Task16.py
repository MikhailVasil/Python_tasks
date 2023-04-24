# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь 
# в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя 
# строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
n = int(input("Enter list size: "))
list_1 = []
count = 0
for i in range(n):
    list_1.insert(0,random.randint(-10, 10))
print(list_1)
x = int(input("Enter number to search: "))
for i in range(len(list_1)):
    if x == list_1[i]:
        count+=1
print(count)