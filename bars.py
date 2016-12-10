# -*- coding: utf-8 -*-

import json
import os
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    else:
        with open (filepath) as input_datas:
            loaded_data=json.load(input_datas)
            return loaded_data

def get_biggest_bar(data):
    bars_seats_count={}
    print('Наибольшее число мест')
    for bar in data:
        bars_seats_count[bar['Cells']['Name'],\
                         bar['Cells']['Address']]=bar['Cells']['SeatsCount']
    for bar, seats_count in bars_seats_count.items():
        if seats_count==max(bars_seats_count.values()):    
            print('%d в баре %s по адресу %s\n' \
                   %(seats_count,bar[0],bar[1]))
    
def get_smallest_bar(data):
    bars_seats_count={}
    print('Наименьшее число мест')
    for bar in data:
        bars_seats_count[bar['Cells']['Name'],\
                         bar['Cells']['Address']]=bar['Cells']['SeatsCount']
    for bar, seats_count in bars_seats_count.items():
        if seats_count==min(bars_seats_count.values()):
            print('%d в баре %s по адресу %s\n' \
                 %(seats_count,bar[0],bar[1]))

def check_coordinates(coordinates):
    try:
        float(coordinates[0]) and float(coordinates[1])
        return coordinates[0], coordinates[1]
    except:
        ValueError or TypeError
        return None

def get_closest_bar(data, longitude, latitude):
    print('Ближайший к Вам')
    bar_coordinates={}
    bar_distance={}
    for bar in data:
        bar_coordinates[bar['Cells']['Name'],\
                        bar['Cells']['Address']]=bar['Cells']['geoData']['coordinates']
    for bars, seats in bar_coordinates.items():
        bar_distance[bars]=math.sqrt((float(longitude)-bar_coordinates[bars][0])**2+\
                                      (float(latitude)-bar_coordinates[bars][1])**2)
    for address, distance in bar_distance.items():
        if distance==min(bar_distance.values()):
            print('%s по адресу %s' %(address[0],address[1]))
        
if __name__ == '__main__':
    filepath=input('Введите абсолютный путь до файла: ')
    if load_data(filepath) is not None:
        get_biggest_bar(load_data(filepath))
        get_smallest_bar(load_data(filepath))
        coordinates=input('Введите Ваши координаты через запятую: ').split(',')
        if check_coordinates(coordinates)==None:
            print('Координаты введены некорректно')
        else:    
            get_closest_bar(load_data(filepath), coordinates[0], coordinates[1])      
    
    else:
        print('Вы ввели неверный путь или имя файла')
