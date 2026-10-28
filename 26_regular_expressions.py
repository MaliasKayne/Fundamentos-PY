## Expresiones regulares ##
#RegEx, ayuda a encontrar patrones en los datos
#match() -> buscar solo al inicio de una cadena,(si hay coincidencias)
#search() -> busca en cualquier parte de la cadena
#findall() -> devuelve una lista con todas las coincidencias
#split() -> recibe una cadena y devuelve una lista dividida en los puntos donde hubo coincidencias
#sub() -> reemplaza una o mas coincidencias
import re

#Match
txt = 'I love to teach python and javascript'
match = re.match('I love to teach', txt, re.I) #patron, texto a buscar, flags, I = ignorar si es mayus o minus
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

#search
txt = '''Python is the most beautiful language that a human being has ever created. Irecommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)
#El resto es lo mismo que el ejemplo anterior
