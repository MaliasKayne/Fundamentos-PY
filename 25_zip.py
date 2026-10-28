##combinar listas con zip ##
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomate', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruits':f, 'vegetables':v})
print(fruits_and_veges)