#funciones integradas de orden superior, map()
from functools import reduce

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

numbers_square = map(square, numbers)
print(list(numbers_square))

numbers_square = map(lambda x : x ** 2, numbers)
print(list(numbers_square))

#funcion de filtro, filter() llama a la funcion especifica y devuelve un valor booleano para cada elemento que cumpla con cierto criterio
numbers = [1, 2, 3, 4, 5]
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

#funcion reduce(), reduce un iterable a un unico valor
numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)