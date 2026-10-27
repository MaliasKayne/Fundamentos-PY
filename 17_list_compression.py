## compresion de listas ##
language = 'python'

lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

#lista de rango de numeros
numbers = [ i for i in range(11)]
print(numbers)

#lista de numeros cuadraticos
squares = [i * i for i in range(11)]
print(squares)

#tupla de numeros cuadrados
numbers = [(i, i * i) for i in range(11)]
print(numbers)

even_numbers = {i for i in range(21) if i % 2 == 0}
print(even_numbers)

#Funcion Lambda
#Es una funcion anonima pequeña y sin nombre
#Puede aceptar cualquier numero de argumentos
#solo puede contener una expresion

def add_two_nums(a,b):
    return a + b

add_two_nums_lambda = lambda a, b: a + b
print(add_two_nums_lambda(2, 3))

#funcion lambda autoinvocada(self-invocking)
print((lambda a, b: a + b)(2, 3))

#operaciones matematicas simples
square = lambda x: x ** 2
print(square(3))

#funcion lambda dentro de otra funcion
def power(x):
    return lambda n: x ** n

cube = power(2)(3) #la funcion requiere de dos argumentos, estos deben ser separados por parentesis
print(cube)