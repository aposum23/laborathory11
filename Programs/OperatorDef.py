#Определение функци
def countFood():
    a = int(input())
    b = int(input())
    print('Всего', a+b, 'шт.')


#Использование функции
print('Сколько бананов и ананасов для обезьян?')
countFood()
print('Сколько жуков и червей для ежей?')
countFood()
print('Сколько рыб и моллюсков для выдр?')
countFood()



#Неправильное использование и объявление функции
print('Сколько бананов и ананасов для обезьян?')
countFood()
print('Сколько жуков и червей для ежей?')
countFood()
print('Сколько рыб и моллюсков для выдр?')
countFood()


def countFood():
    a = int(input())
    b = int(input())
    print('Всего', a+b, 'шт.')
"""
Сколько бананов и ананасов для обезьян?
Traceback (most recent call last):
    File OperatorDef.py, line 20, in <module>
        countFood()
NameError: name 'countFood' is not defined
"""