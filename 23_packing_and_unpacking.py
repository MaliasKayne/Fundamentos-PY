## empacar y desempacar parametros ###
#Se usan dos operadores
# * -> se usan para las tuple/list, ** -> dict
def sum_of_five_numbers(a,b,c,d,e):
    return a + b + c + d + e

lst =[1,2,3,4,5]
print(sum_of_five_numbers(*lst))

#desempaquetar con range()
numbers = range(2,7)
print(list(numbers))
args = [2,7]
numbers = range(*args)
print(list(numbers))

#desempaquetado en asignaciones
countries = ['Finland', 'Sweden', 'Norway', 'Germany', 'USA']
fin, sw, nor, ger, *rest = countries

numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one, middle, last)

#desempaquetar dict
def unpacking_person_info(name, country, city, age):
    return f'{name} vive en {city}, {country}. Tiene {age} años.'
dct = {'name': 'Jossie', 'country': 'Colombia', 'city': 'Puerto Asis', 'age':22}
print(unpacking_person_info(**dct))

#expandir
lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)