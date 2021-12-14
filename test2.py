#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:38:12 2021

@author: rostmaxymchuk@gmail.com
"""

from collections import defaultdict

d = defaultdict(list)
li = [1,2,3,4]

print(("\n\n Приветствую! \n\n "
        "Эта программа сохраняет задания на нужный день"))

while True:
    
    try:
    
        b = int(input((" 1 :  Хотите добавить задание?\n "
                "2 :  Хотите удалить ОДНО задание за конкретный день?\n "
                "3 :  Хотите удалить ВСЕ задание за конкретный день?\n "
                "4 :  Просмотреть все внесённые задания\n "
                "* :  Выйти из программы - любой символ\n\n"
                "Ваш ответ: ")))
    
    except ValueError:
        
        print("\n Спасибо, что воспользовались программой\n\n     Good luck!")
        break

    if b in li :
        if b == 1:

                d[str(input(' На какой день записать? (ДД-ММ-ГГГГ): '))].append(str(input('Введите Ваше задание: ')))
                print('\n Ваше задание записано')
                continue
            
        elif b == 2:
            
            print("\n У Вас актуальными есть следующие задания:\n")
            
            for key, values in d.items():
                print(key, end=':\n .. \n')
                for value in values:
                    print(value)
                print('—————————————\n')
            
            try:
                k = d[input('Укажите день в формате ДД-ММ-ГГГГ из которого нужно удалить задание\n ')]
                k.pop(k.index(input('Введите задание для удаления: ')))
                
                print("\n У Вас остались актуальными следующие задания:\n")
            
                for key, values in d.items():
                    print(key, end=':\n .. \n')
                    for value in values:
                        print(value)
                    print('—————————————\n')
                
            except ValueError:
                print("\n Такого задания нет в базе")
                continue

        elif b == 3:
            try:
            
                print("\n У Вас актуальными есть следующие задания:\n")
            
                for key, values in d.items():
                    print(key, end=':\n .. \n')
                    for value in values:
                        print(value)
                    print('—————————————\n')
                        
                del d[input("Укажите за какой день (ДД-ММ-ГГГГ) все задания выполены и их нужно удалить: ")]
                print("\n Все задания за указаный день удалены")
                continue
            
            except KeyError:
                print("\n Такого задания нет в базе")

        elif b == 4:
                print("\n У Вас актуальными есть следующие задания:\n")
            
                for key, values in d.items():
                    print(key, end=':\n .. \n')
                    for value in values:
                        print(value)
                    print('—————————————\n')
                continue

    else:
        print("\n Спасибо, что воспользовались программой\n\n     Good luck!")
        break
