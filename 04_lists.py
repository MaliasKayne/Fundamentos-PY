my_list = []

print(len(my_list))

my_list = [35, 23, 53, 65, 23, 56]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.70, "Jossie", "Diaz"]

print(type(my_list))
print(type(my_other_list))

#Acceso a elementos y busqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[4])

print(my_other_list.index("Jossie"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

#concatenacion
print(my_list + my_other_list)

#contar
print(my_list.count(23))

#Crear, insertar, actualizar y eliminar
my_other_list.append("Jos")
print(my_other_list)

my_other_list.insert(1, "Rojo") #insertar un valor en la posicion indicada
print(my_other_list)

my_other_list[1] = "Azul" #Actualizar/modificar en el indice indicado
print(my_other_list)

my_other_list.remove("Azul") #Eliminar
print(my_other_list)

my_list.remove(23)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

#del my_list[2]
#print(my_list)

#del my_list elimina completamente la lista
#print(my_list)

#operaciones con listas
my_new_list = my_list.copy() #creo una copia independiente
my_list.clear() #vacia la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #invierte el orden de los elementos
print(my_new_list)

my_new_list.sort() #ordena los elementos de menor a mayor
print(my_new_list)

#sublistas
print(my_new_list[1:3])

#Cambio de tipo
my_list = "Hola Python"
print(my_list)