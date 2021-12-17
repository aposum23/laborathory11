#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


def add_element():
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = datetime.strptime(input('Время отправления: '), '%Y-%m-%d %H:%M')
    trains = {}
    trains['name'] = name
    trains['num'] = int(num)
    trains['tm'] = tm
    return trains


def find_train(trains):
    num = int(input('Введите номер искомого поезда: '))
    for dcts in trains:
        if dcts['num'] == num:
            print(f'Конечный пункт: {dcts["name"]} \n'
                  f'Номер поезда: {dcts["num"]} \n'
                  f'Время отправления: {(dcts["tm"])}')
            return
    print('Поезда с таким номером нет')


if __name__ == '__main__':
    flag = True
    trains = []
    while flag:
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            trains.append(add_element())
        elif com == 2:
            find_train(trains)
        elif com == 3:
            flag = False