# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е.з не
# меньше заданного минимума и не больше заданного максимума)

import random


def random_list(n,min,max):
    list_1 = list()
    for i in range(n):
         list_1.append(random.randint(min,max))
    return(list_1)


n = int(input("Enter the length of the list: "))
min = int(input("Enter the min element of the list: "))
max = int(input("Enter the max element of the list: "))
list_1 = random_list(n,min,max)
print(list_1)
count = 0
min1 = int(input("Enter the min search range: "))
max1 = int(input("Enter the max search range: "))

for i in list_1:
    if min1<=i<=max1: 
        print(count)
    count+=1