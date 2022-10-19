import random

a = []     #Вариант 2 (задание 1 и 2)
b = []
c = []
print('Введите количество элементов в массиве')
n = int(input())
for i in range(n):
    print('Введите', i, 'элемент:')
    a.append(int(input()))
print(a)
print(min(a))
print(a.index(min(a)))
for i in range(len(a)):
    if a[i] >= 0:
        b.append(a[i])
for i in range(len(a)):
    if a[i] >= 0:
        b.append(a[i])
print(b)
c = list(set(a)-set(b))
print(c)


a = [random.randint(-100, 100) for i in range(10)]     #Вариант 4 (задание 1)
print(a)
print(max(a))
print(a.index(max(a)))


a = [random.randint(0, 100) for i in range(10)]     #Вариант 4 (задание 2)
print(a)
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
if len(b) == 0:
    print('Нечётных чисел нет')
print(sorted(b, reverse = True))


from math import prod     #Вариант 7 (задание 1)
a = [random.randint(0, 100) for i in range(10)]
print(sum(a[::2]))
print(prod(a[1::2]))


a = [random.randint(0, 100) for i in range(10)]     #Вариант 7 (задание 2)
print(a)
ma = max(a)
mi = min(a)
a[0] = ma
a[len(a)-1] = mi
print(a)
