import math


def pl(figur, data):    #Вариант 1
    if figur == 'круг':
        print(data[0])
        result = 3.14 * (data[0] ** 2)
    if figur == 'квадрат':
        a = data
        result = a * a
    if figur == 'треугольник':
        a, b = data
        result = (a * b) / 2
    return ' Площадь {} = {}'.format(figur, result)


figur = input('Введите название фигуры: ')
data = [int(i) for i in input('Введите данные через пробел: ').rsplit()]
print(pl(figur, data))




def tr1(kat1, kat2):    #Вариант 3 (задание 1)
    kgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kgip)
    return gip


def tr2(kat1, kat2):
    kgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kgip)
    return gip


if tr1(7, 4) > tr2(4, 13):
    print("Первая больше")
else:
    print("Вторая больше")



    
def preobr(text):    #Вариант 3 (задание 2)
    return " ".join(map(lambda x: ''.join(sorted(list(x))), text.split()))


print(preobr("С новым годом"))
