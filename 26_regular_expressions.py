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
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)
#El resto es lo mismo que el ejemplo anterior

#Buscar todas las coincidencias con findall
matches = re.findall('language', txt, re.I)
print(matches)

#Reemplazar subcadenas
match_replaced = re.sub('Python|python', 'Javascript', txt, re.I)
print(match_replaced)

#RegEx para dividir el texto
txt = '''I am a teacher and I love teaching. 
There is nothing as regarding as education and empowering people.
I found teaching more interesting than any other jobs
Does this motivate you to be a teacher?
'''

print(re.split('\n', txt)) #dividir txt usando \n -salto de linea

#construir patrones RegEx
regex_patern = r'[Aa]pple|[Bb]anana' #Raw string -> trata las barras invertidas como texto literal
txt = 'Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away, has been replaced by a banana a day keeps the doctor away'

regex_patern = r'[a-zA-z0-9]' #caracteres de la a a la z...
matches = re.findall(regex_patern, txt)
print(matches)


regex_patern = r'\d' #digito individual
txt = 'This regular expresion example was made on April 6, 2026 and revised on October 28, 2026'
matches = re.findall(regex_patern, txt)
print(matches)

regex_patern = r'\d+' #numeros en bloque
matches = re.findall(regex_patern, txt)
print(matches)

regex_patern = r'\\d' #escapar el \
matches = re.findall(regex_patern, txt)
print(matches)

#Punto .
regex_patern = r'[a].' # va a buscar 'a' seguido de cualquier caracter, excepto nueva linea
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_patern, txt)
print(matches)

regex_patern = r'[a].+' # buscara a 'a' seguido de todo lo que venga despues de la linea
matches = re.findall(regex_patern, txt)
print(matches)

# 0 o mas veces (*)
regex_patern = r'[a].*' # buscara 'a' seguida de cualquier caracter cero o mas veces
matches = re.findall(regex_patern, txt)
print(matches)

txt = '''I am not sure if there is a convention in how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail'''
regex_patern = r'[Ee]-?mail' #  '-?' significa opcional
matches = re.findall(regex_patern, txt)
print(matches)

#cuantificadores en RegEx
txt = 'This regular expresion example was made on April 6, 2026 and revised on October 28, 2026'
regex_patern = r'\d{4}' #bloques de 4 numeros
matches = re.findall(regex_patern, txt)
print(matches)

regex_patern = r'\d{1,4}' #bloques de 1 a 4 numeros
matches = re.findall(regex_patern, txt)
print(matches)

#circunflejo (^)
regex_patern = r'^This' #para indicar inicio, que empieza con la palabra 'This'
matches = re.findall(regex_patern, txt)
print(matches)

regex_patern = r'[^A-Za-z ]+' #Dentro de corchetes [], ^ significa negacion, no A-Za-z, no espacio
matches = re.findall(regex_patern, txt)
print(matches)

email = "diazjossie2@gmail.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-z-.]+$'
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))