# Задача 26:  Напишите программу, которая на вход 
# принимает два числа A и B, и возводит число А в 
# целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
    
# n = int(input())
# f = factorial_recursive(n)
# print(f)

def product(a,b):
    if a > 0 and b == 1:
        return a
    elif a > 0 and b > 0:
        return a*product(a,b-1)
    elif a <= 0 or b < 0:
        return "Fail"
    return 1
    
    

print(product(1,0))