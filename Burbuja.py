# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:31:29 2019

@author: Crudist
"""

def Burbuja(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [19,54,26,93,17,77,31,44,55,20]
Burbuja(list)
print("Método Burbuja")
print(list)

