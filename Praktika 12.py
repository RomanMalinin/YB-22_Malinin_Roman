def Factorial(a):    #Блок А  №1
    if a == 0:
        return 1
    else:
        return a * Factorial(a - 1)

x = int(input())
a = int(input())
print(x ** a / Factorial(a))




def posl():    #Блок Б  №1
    a = int(input())
    if a == 0:
        return 0
    else:
        return max(a, posl())
print(posl())
