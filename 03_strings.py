### Strings ###
my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\t Este es un string \\n escapado"
print(my_scape_string)

#Format
name, surname, age = "Jossie", "Diaz", 22
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

print("{} % {} = {}".format(10, 3, 10 % 3))

print("Mi nombre es "+ name +" "+ surname +" y mi edad es "+ str(age))

#f-string, evaluar expresiones dentro del texto
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(e)
print(f)

#Division slicing/rebanando
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

reversed_language = language[::-1]
print(reversed_language)

#Funciones del lenguaje

print(language.capitalize()) #primer letra en mayuscula 
print(language.upper()) #convertir a mayusculas
print(language.count("")) #cuenta cuantas veces aparece una subcadena
print(language.isnumeric()) #Evalua si todos los caracteres son numericos
print("1".isnumeric())
print(language.lower()) #convierte la cadena en minusculas
print(language.lower().isupper()) #convierte en minusculas y valida si la cadena esta en mayusculas
print(language.startswith("py")) #valida si la cadena comienza con la subcadena indicada
print(language.startswith("Py")) #valida si la cadena comienza con la subcadena indicada
print("Py" == "py") #no es lo mismo