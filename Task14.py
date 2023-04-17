# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

print("Input the digit:")
n = int(input())
for i in range (0, n//2-1):
    print (2**i, end=" ")
# i = 0
# while 2**i <= n:
#     print (2**i, end=" ")
#     i+=1