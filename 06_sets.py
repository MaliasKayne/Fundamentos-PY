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

st = {'item 1', 'item 2', 'item 3', 'item 4'}
st.update(['item 5', 'item 6', 'item 7']) #agregar varios elementos
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_items = fruits.pop()
print(removed_items)
print(fruits)

#conversion de un conjunto a lista
my_set = {'Jossie', 'Diaz', 22}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

#otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"}))

st1 = {'item 1', 'item 2', 'item 3', 'item 4'}
st2 = {'item 3', 'item 2'}
print(st1.intersection(st2))

#subconjuntos

print(st2.issubset(st1)) #st2 subconjunto de st1
print(st1.issubset(st2))
print(st1.issuperset(st2)) #st1 supersubconjunto de st2
print(my_new_set.difference(my_set)) #devuelve la diferencia entre dos conjuntos
print(st2.symmetric_difference(st1)) # (A\B U B\A)
print(st2.isdisjoint(st1)) #si son conjuntos disjuntos