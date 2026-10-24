## functions ##
#Definicion
def my_function():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

#function con parametros de entrada/argumentos
def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5,7)
sum_two_values(5445,72134)
sum_two_values("5","7")
#sum_two_values("1.4",1.5)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10,5)
print(my_result)

#Funcion con parametros de entrada o argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}") 

print_name(surname="Diaz", name="Jossie") #Llamado con argumentos por clave

#Funcion con parametros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jossie", "Diaz")
print_name_with_default("Jossie", "Diaz", "Jos")

#Funcion con parametros de entrada/argumentos *args (arbitrarios)
def print_upper_text(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_text("Hola", "Python", "MarlonDev")
print_upper_text("Hola")