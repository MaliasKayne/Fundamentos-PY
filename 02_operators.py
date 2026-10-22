###operadores aritmeticos###
#operaciones con enteros
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

#operaciones con cadenas de texto
print("Hola " + "python " + "que tal?")
print("Hola " + str(5))

#operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))
my_float = 2.5 * 2
print("Hola " * int(my_float))

##operadores comparativos##
#operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Operaciones con cadenas de texto
print("Hola" > "Python")  #En codigo ASCII los caracteres tienen un valor, python compara esos valores al usar operadores con cadenas de texto
print("Hola" < "Python")
print("aaaa" >= "abaa") #Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #cuenta los caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

#operadores logicos
print(3 < 4 and "hola" > "Python")
print(3 > 4 or "hola" > "Python")
print(3 > 4 or "hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))