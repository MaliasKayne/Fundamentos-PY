### maejo de archivos ###
#open(`filename`, mode) r -> read,lectura, a -> append, w -> write,escritura, x -> create, crear, t -> text, texto, b -> binario (imagenes)
#mode -> por defecto es lectura (r)
import os, json, csv
import openpyxl
import xml.etree.ElementTree as ET

f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.readline() #lee solo la primera linea
print(type(lines))
print(lines)
f.close()


f = open('./files/reading_file_example.txt')
lines = f.readlines() #lee todo el texto linea por linea
print(type(lines))
print(lines)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.read().splitlines() #lee solo la primera linea
print(type(lines))
print(lines)
f.close()

with open('./files/reading_file_example.txt', 'w') as f:
    f.write('Este texto debe anadirse al final') # W crea el archivo si no existe y sobre escribe lo que hay dentro si existe.

with open('./files/reading_file_example.txt', 'a') as f:
    f.write('Este texto debe anadirse al final') # a append 

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('El archivo no existe')

#Archivos con extension json
person_dct = {
    "name":"Jossie",
    "country":"Colombia",
    "city":"Puerto Asis",
    "skills": ["Javascript", "VueJS", "Python"]
}
#cadena json valida
person_json = '''{
    "name":"Jossie",
    "country":"Colombia",
    "city":"Puerto Asis",
    "skills": ["Javascript", "VueJS", "Python"]
}'''
person_dct = json.loads(person_json) #convierto la cadena json a dict
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
#convertir de dict a json
person_json = json.dumps(person_dct, indent=4) #la identacion puede ser 2, 4, 8
print(type(person_json))
print(person_json)

#guardar archivo json
person = {
    "name":"Jossie",
    "country":"Colombia",
    "city":"Puerto Asis",
    "skills": ["Javascript", "VueJS", "Python"]
}
with open('./files/json_example.json','w',encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4) #json.dump(dict, file, notificacion para evitar errores de codificacion, identacion)
    #ñ \u00f1
with open('./files/json_example.json','r',encoding='utf-8') as f:
    file_json = json.load(f)
    print(file_json)

#archivos con extension csv (Comma Separated Values) datos tabulares

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',',) #Crea el archivo si no existe
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Encabezados: {",".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} {row[1]}, {row[2]}, {row[3]}')
            line_count += 1
    print(f'Procesadas: {line_count} lineas.')
f.close()

with open('./files/csv_example.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    #escribe encabezados
    writer.writerow(['name','country','city','skills'])
    #ecribe los datos
    writer.writerow(['Jossie','Colombia','Puerto Asis','Python'])
    writer.writerow(['Paola','Venezuela','Caracas','C#'])
    writer.writerow(['Jaimito','Peru','Lima','PHP'])
f.close()

#archivos escel xlrd -> xls, openpyxl, pandas -> xlsx
#comando para instalar openpyxl (opcional pandas), pip install openpyxl pandas
#crear un libro nuevo
os.makedirs('./files', exist_ok=True)
ruta_guardado = './files/mi_reporte.xlsx'
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Reporte'
sheet.append(["ID", "Nombre", "Rol"])
sheet.append(["1", "Luis", "Diseñador"])
sheet.append(["2", "Hugo", "Analista"])
sheet.append(["2", "Paco", "Desarrollador"])
wb.save(ruta_guardado)
print(f'Archivo guardado exitosamente en: {ruta_guardado}')

#lectura de un archivo xlsx
wb = openpyxl.load_workbook('./files/mi_reporte.xlsx') #cargo el libro
print("Hojas: ", wb.sheetnames) #Hojas disponibles
sheet = wb.active #wb.active['Reporte'] <- si hay muchas hojas en el libro se puede especificar la hoja activa
print("Valor de A1: ", sheet['A1'].value)
print("Valor en fila 2, columna 1: ", sheet.cell(row=2, column=1).value)

for row in sheet.iter_rows(values_only=True): #recorrer las filas
    print(row) #mostrar cada fila como tupla

#archivos con extencion xml
tree = ET.parse('./files/xml_example.xml') #leer el archivo
root = tree.getroot() #obtener el nodo raiz del nodo de datos (person)

print('Etiqueta raiz: ', root.tag) #salida de person
print('Atributos: ', root.attrib) #salida de gender
for child in root: #recorrer los hijos directos del nodo
    print('Campo: ', child.tag)
    if(child.tag != 'skills'):
        print(child.text)
    else:
        for skill in child:
            print(skill.text)