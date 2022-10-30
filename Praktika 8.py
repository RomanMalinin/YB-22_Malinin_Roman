import random

pl = 0    #Вариант 1 (задание 1)
s = 0
N = int(input('Введите число: '))
A = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pl += 1
            s += A[i][j]
print('Сумма положительных элементов матрицы:', s)
print('Число положительных элементов матрицы:', pl)



N = int(input('Введите первое число: '))    #Вариант 1 (задание 2)
M = int(input('Введите второе число: '))
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
for i, row in enumerate(B):
    max = min = 0
    for j, el in enumerate(row):
        if el > row[max]:
            max = j
        if el < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(B)



N = int(input('Введите размер матрицы: '))    #Вариант 4 (задание 1)
A = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range (N): print( * A[i])

maxs = [0] * N
for i in range (N):
    maxs[i] = sum(A[i])
print ('Максимальная cтрока:', maxs.index (max(maxs)) + 1, ', сумма строки:', max(maxs))
print ('Минимальная cтрока:', maxs.index (min(maxs)) + 1, ', сумма строки:', min(maxs))



a = [[4, -5, 6],    #Вариант 4 (задание 2)
     [4, 5, -6],
     [-4, 5, 6]]
a = [[1 if x > 0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))],'')
