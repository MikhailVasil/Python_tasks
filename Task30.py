# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(a1, n, d):
    
    progr = list()
    for i in range(1,n+1):
        progr.append(a1 + ((i-1)*d))
    return progr


a1 = int(input("Enter the first element: "))
n = int(input("Enter the length of the list: "))
d = int(input("Enter difference of elements: "))
prog1 = arithmetic_progression(a1,n,d)
print(prog1)

