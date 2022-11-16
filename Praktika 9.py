with open('Matrix1.txt', 'r', encoding='utf-8-sig') as f:
	line = f.readlines()
	matrix = [element.replace("\n", "").split() for element in line]
n = len(matrix)
m = len(matrix[0])
a = matrix
f.close()
for p in range(n):
	for u in range(m):
		a[p][u] = int(a[p][u])
print(a)



pl = 0    #Вариант 1 (задание 1)
s = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] <= 0:
           continue
        if a[i][j] > 0:
            pl += 1
            s += a[i][j]
print('Сумма положительных элементов матрицы:', s)
print('Число положительных элементов матрицы:', pl)
p = open('Res.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write("Sum: " + str(s) + " Chilso polozh. elem.: " + str(pl))
p.close()



N = int(input('Введите первое число: '))    #Вариант 1 (задание 2)
M = int(input('Введите второе число: '))
for i, row in enumerate(n):
    max = min = 0
    for j, el in enumerate(row):
        if el > row[max]:
            max = j
        if el < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(n)
p = open('Res.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write(str(n))
p.close()



for i in range (n):    #Вариант 4 (задание 1)
    print( * a[i])    
maxs = [0] * n
for i in range (n):
    maxs[i] = sum(a[i])
print ('Максимальная cтрока:', maxs.index (max(maxs)) + 1, ', сумма строки:', max(maxs))
print ('Минимальная cтрока:', maxs.index (min(maxs)) + 1, ', сумма строки:', min(maxs))
p = open('Res.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write("Max str: " + str(maxs.index (max(maxs)) + 1) + ", sum str: " + str(max(maxs)) + " Min str: " + str(maxs.index (min(maxs)) + 1) + ", sum str: " + str(min(maxs)))
p.close()



a = [[1 if x > 0 else 0 for x in i] for i in a]    #Вариант 4 (задание 2)
for i in range(len(a)):
    print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))],'')
p = open('Res.txt', 'w')
for z in range(n):
	for v in range(n):
		l = str(a[z][v])
		p.write(l + '  ')
	p.write('\n')
p.write(str(*[a[i][x] if x <= i else '' for x in range(len(a[i]))],''))
p.close()
