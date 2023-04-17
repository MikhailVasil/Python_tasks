# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное количество 
# монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

import random
n = int(input("Enter n coins: "))
nul=0
one=0
for i in range(n):
    i = random.randint(0,1)
    print (i, end=" ")
    if (i==1):
        one+=1
    else:
        nul+=1
print()
if(one>nul):
    print(nul)
elif(one<nul):
    print(one)
else:
    print(f"{one} the same number of coins")
