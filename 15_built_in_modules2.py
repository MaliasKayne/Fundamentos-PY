import sys

#modulo que me permite acceder a informacion de variables y funciones que interactuan directamente con el interprete de python

print(f"Nombre del script: {sys.argv[0]}")

#Comprobar si se enviaron argumentos adicionales
if len(sys.argv) > 1:
    print(f"Argumentos recibidos {sys.argv[1:]}")
else:
    print("No se pasaron argumentos adicionales.")

#Finalizar la ejecucion
edad = 15
if edad < 18:
    print("Error acceso denegado a menores de edad.")
    sys.exit(1) #Finaliza el script inmediatamente con el estado de error
print("Bienvenido al sistema")