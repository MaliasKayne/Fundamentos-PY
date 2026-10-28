## Enumerar ##
#Si necesitamos los indices de una lisa, usamos la funcion enumerate
for index, item in enumerate([20,30,40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Germany', 'USA']
for index, i in enumerate(countries):
    print('Hola')
    if i == 'Finland':
        print(f'El pais {i} esta en el indice {index}')