#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:29:03 2020

@author: david
"""

import multiprocessing as mp
from time import time
import numpy as np


print("Número de nucleos: {}".format(mp.cpu_count()))

datos=np.random.randint(0,10,size=[10000000,5])#Arreglo de 20000 x 5
datos= datos.tolist() # Lo convertimos a lista. ("20,000 con 5 elementos con numeros aleatorios entre 0 y 10")
datos[:5]


def cuantos_dentro_rango(lista,minimo,maximo):
  contador = 0
  for n in lista:
    if minimo <= n <= maximo:
      contador = contador +1
  return contador 

resultado = []

for lista in datos:
  resultado.append(cuantos_dentro_rango(lista,minimo= 4,maximo=8))

print(resultado[:5])


pool=mp.Pool(mp.cpu_count())
inicio = time()
resultado = [pool.apply(cuantos_dentro_rango,args=(lista,4,8)) for lista in datos] #Para cada lista en datos.
print(resultado[:5])
t_transcurrido = time()-inicio
pool.close()
print(t_transcurrido)


def cuantos_dentro_rango_map(lista,minimo=4,maximo=8):
  contador = 0
  for n in lista:
    if minimo <= n <= maximo:
      contador=contador+1
  return contador

pool=mp.Pool(mp.cpu_count())
inicio = time()
resultado = pool.map(cuantos_dentro_rango_map,[lista for lista in datos])
print(resultado[:5])
t_transcurrido = time()-inicio
pool.close()
print(t_transcurrido)