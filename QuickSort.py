# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:04:33 2019

@author: Crudist
"""

def QuickSort(list):
    izq = []
    cen = []
    der = []
    if len(list) > 1:
        pivote = list[0]
        for i in list:
            if i < pivote:
                izq.append(i)
            elif i == pivote:
                cen.append(i)
            elif i > pivote:
                der.append(i)
        return QuickSort(izq)+cen+QuickSort(der)
    else:
      return list

list = [19,54,26,93,17,77,31,44,55,20]
print("Método Quick Sort")
print(QuickSort(list))


