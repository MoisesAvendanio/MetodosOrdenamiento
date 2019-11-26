# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:56:42 2019

@author: Crudist
"""

def Mezcla(list):
    #print("Mitad ",list)
    if len(list)>1:
        mitad = len(list)//2
        mIzq = list[:mitad]
        mDer  = list[mitad:]

        Mezcla(mIzq)
        Mezcla(mDer )

        i=0
        j=0
        k=0
        while i < len(mIzq) and j < len(mDer ):
            if mIzq[i] < mDer [j]:
                list[k]=mIzq[i]
                i=i+1
            else:
                list[k]=mDer [j]
                j=j+1
            k=k+1

        while i < len(mIzq):
            list[k]=mIzq[i]
            i=i+1
            k=k+1

        while j < len(mDer ):
            list[k]=mDer [j]
            j=j+1
            k=k+1
    #print("Ordena ",list)

list = [19,54,26,93,17,77,31,44,55,20]
print("Método Mezcla")
Mezcla(list)
print(list)


