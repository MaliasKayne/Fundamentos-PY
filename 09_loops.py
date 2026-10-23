## loops ##
#While
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("Mi condicion es mayor o igual a 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break
    print(my_condition)

#for
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (22, 1.70, "Jossie", "Diaz", "Jos")
for element in my_tuple:
    print(element)

my_set = {"Jossie", "Diaz", 22}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Jossie",
    "Apellido": "Diaz",
    "Edad": 22,
    "Languages": {"Python", "Swift", "Kotlin"},
    1: 1.70
}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
        print("oeeeee")
    print("Se ejecuta")
else:
    print("El bucle for para el diccionario ha finalizado")

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(key, value)
