## Sets ##
#Definicion

my_set = set() #conjunto
my_other_set = {}

print(type(my_set))

my_other_set = {
    "Jossie",
    "Diaz",
    22
}

print(type(my_other_set))
print(len(my_other_set))

#Insercion
my_other_set.add("Jos")
print(my_other_set) #un set no es una estructura ordenada

my_other_set.add("Jossie")
print(my_other_set)

#busqueda
print("Jossie" in my_other_set)
print("Josie" in my_other_set)

#eliminacion
my_other_set.remove("Diaz")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set