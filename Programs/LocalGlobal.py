def rectangle():
    a = float(input('Ширина: '))#Это локальная переменная
    b = float(input('Высота '))#Это локальная переменная
    print(f' {a * b}')


def triangle():
    a = float(input('Основание: '))#Это локальная переменная
    h = float(input('Высота: '))#Это локальная переменная
    print(f' {0.5 * a * h}')



figure = input('1-прямоугольник, 2-треугольник: ') #Это глобальная переменная

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()




result = 0#Это глобальная переменная


def rectangle():
    a = float(input('Ширина: '))#Это локальная переменная
    b = float(input('Высота '))#Это локальная переменная
    result = a * b


def triangle():
    a = float(input('Основание: '))#Это локальная переменная
    h = float(input('Высота: '))#Это локальная переменная
    result = 0.5 * a * h



figure = input('1-прямоугольник, 2-треугольник: ') #Это глобальная переменная

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print('Площадь: %.2f%' % result)