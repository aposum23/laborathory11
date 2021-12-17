import math


def cylinder():
    r = float(input())
    h = float(input())
    side = 2* math.pi * r * h
    circle = math.pi * r**2
    full = side + 2 * circle
    return full


square = cylinder()
print(square)
"""
3
7
188.4
"""




import math


def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
        return

    side = 2* math.pi * r * h
    circle = math.pi * r**2
    full = side + 2 * circle
    return full


print(cylinder())





#Возврат нескольких значенией
import math


def cylinder():
    r = float(input())
    h = float(input())
    side = 2 * math.pi * r * h
    circle = math.pi * r**2
    full = side + 2 * circle
    return side, full


scyl, fcyl = cylinder()
print(f'Площадь боковой поверхности{scyl}')
print(f'Полная площадь{fcyl}')
