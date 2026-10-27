import os
import sys

#modulo que me permite acceder a informacion de variables y funciones que interactuan directamente con el interprete de python

print(f"Nombre del script: {sys.argv[0]}")

#Comprobar si se enviaron argumentos adicionales
if len(sys.argv) > 1:
    print(f"Argumentos recibidos {sys.argv[1:]}")
else:
    print("No se pasaron argumentos adicionales.")

#Finalizar la ejecucion
edad = 18
if edad < 18:
    print("Error acceso denegado a menores de edad.")
    #sys.exit(1) #Finaliza el script inmediatamente con el estado de error
print("Bienvenido al sistema")

#Rutas de Busqueda de Modulos
print("Rutas de importacion: ")
for ruta in sys.path:
    #Viendo las rutas actuales donde python busca librerias
    print(ruta)

#Agregar una ruta personalizada para importar un modulo propio
#sys.path.append("C:/JossieDiaz/Workspace/Fundamentos-PY")
#sys.path.append("C:\JossieDiaz\Workspace\Fundamentos-PY") #Raw strings, quiere decir que python interpreta las rutas literalmente
#sys.path.append("C:\\JossieDiaz\\Workspace\\Fundamentos-PY") #Escapando las barras

#La forma avanzada de hacerlo
ruta_modulo = os.path.join(os.getcwd(), "mis_modulos")

#verificar y crear la carpeta fisica en el disco
if not os.path.exists(ruta_modulo):
    os.mkdir(ruta_modulo)
    print(f"\n[+] se ha creado fisicamente la carpeta {ruta_modulo}")
else:
    print(f"\n[*] la carpeta ya existe en el disco duro: {ruta_modulo}")
sys.path.append(ruta_modulo)
print("[+] Ruta añadida a sys.path correctamente")

print("Rutas de importacion: ")
for ruta in sys.path:
    #Viendo las rutas actuales donde python busca librerias
    print(ruta)

#informacion del entorno 
print(f"Version de python: {sys.version}")
print(f"Plataforma detectada: {sys.platform}")

#logica condicional segun el sistema operativo
if sys.platform.startswith("win32"):
    print("Ejecutandose en windows")
elif sys.platform.startswith("linux"):
    print("Ejecutandose en Linux / WSL")
elif sys.platform == "darwind":
    print("Ejecutandose en macOS")

#flujos de entrada y salida con sys

sys.stdout.write("hola desde stdout\n") #Salida estandar == print
sys.stderr.write("Advertencia! Ocurrio un fallo en el proceso. \n")

#uso de memoria
lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)

print(f"Tamaño lista en memoria: {sys.getsizeof(lista)} bytes")
print(f"Tamaño tupla en memoria: {sys.getsizeof(tupla)} bytes")
