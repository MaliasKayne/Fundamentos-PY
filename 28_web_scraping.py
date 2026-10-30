##Web scraping ##
#Extraer y recopilar datos de sitios web y almacenarlos en mi equipo local o en una base de datos
#pip install requests
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com' #url activa para practicas de web scraping
response = requests.get(url) #usando la peticion get para obtener datos
status = response.status_code
print("Estado HTTP: ", status)

content = response.content #obtengo el contenido crudo de la respuesta
soup = BeautifulSoup(content, 'html.parser') #parsear al arbol html
print("Tag title: ", soup.title)
print("Texto del title: ", soup.title.get_text().strip()) #Extraer el titulo tipo texto, tambien elimina espacios en blanco

articles = soup.find_all('article', class_='product_pod') #traigo los tag article que tengan la clase product_pod
first_book = articles[0] #tomando el primer libro
title = first_book.find('h3').find('a')['title']
price = first_book.find('p', class_='price_color').text

print(f'\nPrimer Libro Encontrado')
print(f'Titulo: {title}')
print(f'Precio: {price}')