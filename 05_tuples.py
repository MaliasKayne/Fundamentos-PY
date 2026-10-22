##tuples##
#Definition - similar a list, pero no se puede cambiar
my_tuple = tuple() #La funcion para construir una tupla
my_other_tupla = tuple()

my_tuple = (22, 1.70, "Jossie", "Diaz", "Jos")
my_other_tupla = (23, 53, 35)

print(my_tuple)
print(my_other_tupla)
print(type(my_tuple))

#acceso a elementos y busqueda

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Jossie"))
print(my_tuple.index("Diaz"))
print(my_tuple.index("Jossie"))

#my_tuple[1] = 1.80 Las tuplas no soportan cambios, se suelen utilizar con arreglos que no se deben cambiar

#concatenacion
my_sum_tuple = my_tuple + my_other_tupla
print(my_sum_tuple)

#subtuples
print(my_sum_tuple[3:6])

#tuple mutable con conversion a lista
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[4] = "JossieDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

print('Azul' in my_tuple) #deberia retornar true

#Eliminacion
#del my_tuple[2] Tuples son inmutables
del my_tuple