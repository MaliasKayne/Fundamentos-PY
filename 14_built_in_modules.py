### Built-in modules ##
#Modulos incorporados Math, datetime, os, sys, stats, collections, json, re, etc

import os

#os.mkdir('files') #crear directorio
directorio_inicial = os.getcwd() #obtener el directorio de trabajo
print(f"Directorio inicial: {directorio_inicial}")

nombre_directorio = "files"
#os.mkdir(nombre_directorio) #Crear directorio
print(f"Directorio '{nombre_directorio}' creado con exito.")

#cambiar el directorio actual
nueva_ruta = os.path.join(directorio_inicial, nombre_directorio)
os.chdir(nueva_ruta)
print(f"Directorio de trabajo actual cambiado a: {os.getcwd()}")

#volver al directorio inicial
os.chdir(directorio_inicial)
print(f"De regreso al directorio inicial: {os.getcwd()}")

#eliminar el directorio creado
os.rmdir(nombre_directorio)
print(f"Directorio '{nombre_directorio}' eliminado correctamente.")