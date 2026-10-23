### Diccionarios ###
##Definicion
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#un diccionario puede tener valores de cualquier tipo: cadena, booleano, lista, tupla, conjunto, diccionario
my_other_dict = {
    "Nombre": "Jossie",
    "Apellido": "Diaz",
    "Edad": 22,
    1: "Python"
}
my_dict = {
    "Nombre": "Jossie",
    "Apellido": "Diaz",
    "Edad": 22,
    "Languages": {"Python", "Swift", "Kotlin"},
    1: 1.70
}
print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

#busqueda
print(my_dict[1])
print(my_dict["Nombre"])
print("Jossie" in my_dict)
print("Apellido" in my_dict)
print(my_dict.get('Languages'))

#insercion
my_dict["address"] = "Calle 13 #34-22"
print(my_dict)

#actualizar
my_dict["Nombre"] = "Alejandro"
print(my_dict)

#Eliminar
del my_dict["address"] #Elimina un elemento con un nombre clave especifico
print(my_dict)

dct = {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3', 'key4': 'Value4'}
print(dct.pop('key1'))
print(dct)
print(dct.popitem()) #Remueve el ultimo elemento
print(dct)

#convertir un diccionario en una lista de tuplas
print(dct.items())

#limpiar un diccionario
print(dct.clear()) #none

#copiar un diccionario
my_dict2 = my_dict.copy()
print(my_dict2)

#obtener claves de un diccionario
keys = my_dict.keys()
print(keys)

#obtener los valores de un diccionario
values = my_dict.values()
print(values)

#nuevo diccionario con claves
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict), "JossieDev")
print(my_new_dict)
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))