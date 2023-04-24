# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input("Enter list size: "))
list_1 = []
for i in range(n):
    list_1.insert(0,random.randint(-10, 10))
print(list_1)
x = int(input("Enter number to search: "))

result = list_1[0]
for i in range(1, len(list_1)):
    if abs(list_1[i] - x) < abs(result-x):
        result = list_1[i]
print(result)
 