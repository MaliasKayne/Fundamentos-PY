## statistics and math module ##
from statistics import * #importando todos los modulos de estadistica
from math import pi, sqrt, pow, floor, ceil, log10
import string
from random import random, randint

ages = [20, 20, 4, 24, 25, 22, 26, 20, 26, 22, 26]
print(mean(ages)) #muestra la media promedio aritmetica
print(median(ages)) #muestra el valor central de la lista cuando los datos estan ordenados de menor a mayor
print(mode(ages)) #muestra el valor que se repite con mayor frecuencia
print(stdev(ages)) #muesta la desviacion estandar muestral

#operaciones matematicas
"""
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3)) #2 ** 3
print(math.floor(9.81)) #Redondeo hacia abajo
print(math.ceil(9.81)) #Redondeo hacia arriba
print(math.log10(100)) #Logaritmo en base 10 del numero ingresado
"""
print(pi)
print(sqrt(2))
print(pow(2,3)) #2 ** 3
print(floor(9.81)) #Redondeo hacia abajo
print(ceil(9.81)) #Redondeo hacia arriba
print(log10(100)) #Logaritmo en base 10 del numero ingresado

#Modulo aleatorio
print(random()) #retorna un valor entre 0 y 0.99999
print(randint(5,20))
