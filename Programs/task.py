#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pandas as pd


def make_table(trains):
    num_lst = []
    end_point_lst = []
    for trn in trains:
        num_lst.append(trn['num'])
        end_point_lst.append(trn['name'])
    data = {'Номер поезда:': num_lst, 'Конечный пункт:': end_point_lst}
    df = pd.DataFrame(data=data)
    print(df)



def add_element():
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = datetime.strptime(input('Время отправления: '), '%Y-%m-%d %H:%M')
    trains = {}
    trains['name'] = name
    trains['num'] = int(num)
    trains['tm'] = tm
    return trains


def find_train(trains, num):
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
        print('\n')
        make_table(trains)
        print('\n')
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            trains.append(add_element())
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            find_train(trains, train_num)
        elif com == 3:
            flag = False
