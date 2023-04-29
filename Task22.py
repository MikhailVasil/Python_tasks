# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются 
# в обоих наборах.  вводит 2 числа. n — кол-во элементов 
# первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random
n = int(input("Enter the length of the list n: "))
n1 = list()
m1 = list()
for i in range(n):
    x=random.randint(-10,10)
    n1.append(x)
print(n1)
m = int(input("Enter the length of the list m: "))
m1 = list()
for i in range(m):
    x=random.randint(-10,10)
    m1.append(x)
print(m1)
n2 = set(n1)
m2 = set(m1)

n2m2 = n2.intersection(m2)
n1m1 = list(n2m2)
tmp = 0 
for j in range(1,len(n1m1)):
    for i in range(0,len(n1m1)-j):
        if (n1m1[i]>n1m1[i+1]):
            tmp = n1m1[i]
            n1m1[i] = n1m1[i+1]
            n1m1[i+1] = tmp          
print(n1m1)

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# print(a)
# k = set(a)
# print(k)
# for i in k:
#     set_1.add(i)
# print(set_1)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 and set_2
# print(lok)
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
