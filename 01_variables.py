### Variables ###

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en un print

print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

print(len(my_string_variable))

#Variables en una sola linea
name, surname, alias, age = "Jossie", "Diaz", "Diaz", 22
print("Me llamo:",name, surname,". Mi edad es:",age,". Y mi alias es:",alias)

#inputs
'''name = input('¿Cuál es tu nombre?')
age = input('Cuantos años tienes?')
print(name)
print(age)
'''
#cambiamos el tipo 
name = 35
age = "Mao"
print(name)
print(age)

#forzamos el tipo
addres: str = "Mi direccion"
addres = True
addres = 5
addres = 1.2
print(type(addres))

#Keywords
help('keywords')

help(str)
