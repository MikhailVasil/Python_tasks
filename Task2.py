# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print ("Enter a three-digit number: ")
a=int(input())
b=a
sum = 0
c=0
if(99<a<1000):
    while(a>0):
        c=a%10
        sum+=c
        a//=10
    print(f"{b} -> {sum}")
else:
    print("Incorrect input")



