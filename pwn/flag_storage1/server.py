#!/usr/bin/env python2
from time import sleep
# -*- coding: utf-8 -*-

print """
#############################################
#                                           #
#          РАСПРЕДЕЛИТЕЛЬ v0.1              #
#                                           #
#############################################
"""
print "Для того чтобы выйти, отправьте 'break'."
print ""

while True:
    print "Введите ваш средний балл: "
    average = input()
    print "Вычисляем место вашего распределения..."
    sleep(2)
    print "Ваш средний балл: ", average
    print "Место вашего распределения: космодром Плесецк"
    print ""