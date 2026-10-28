### manejo de excepsiones Try, except, else, finally ###
try:
    print(10+'5') #si todo va bien
except:
    print("ocurrio un error") # so ocurre un error

#mostramos el error

'''
try:
    name = input('introduce tu nombre:')
    year_born = input('En que ano naciste?')
    age = 2026 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print("Se produjo un error de tipo (TypeError)")
except ValueError:
    print("Se produjo un ValueError")
except ZeroDivisionError:
    print("Se produjo una division por cero (zeroDivisionError)")
'''

#anadir bloques adicionales

'''
try:
    name = input('introduce tu nombre:')
    year_born = input('En que ano naciste?')
    age = 2026 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print("Se produjo un error de tipo (TypeError)")
except ValueError:
    print("Se produjo un ValueError")
except ZeroDivisionError:
    print("Se produjo una division por cero (zeroDivisionError)")
else:
    print('Este bloque se ejecuta normalmente despues del try')
finally:
    print('Este bloque siempre se ejecuta')
'''

#simplificar el manejo de excepciones 
try:
    name = input('introduce tu nombre: ')
    year_born = input('En que ano naciste?: ')
    age = 2026 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except Exception as e:
    print(e)