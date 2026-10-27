## Funciones de orden superior ##
#reciba una o mas funciones como argumentos/parametros
#devuelve otra funcion como resultado

def sum_number(nums): #funcion normal
    return sum(nums) #calcula la suma de los elementos en nums

def higher_order_function(f, lst): #funcion + el parametro
    sumation = f(lst)
    return sumation

result = higher_order_function(sum_number, [1,2,4,5])
print(result)


#como valor de retorno
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function2(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function2('square')
print(result(3))
result = higher_order_function2('cube')
print(result(3))
result = higher_order_function2('absolute')
print(result(-3))

#Cierres, python permite que una funcion anidada acceda al ambito externo de la funcion que la contiene

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))

#decoradores, es una funcion que toma a otra funcion como argumento, extiende o modifica su comportamiento, devuelve una nueva funcion modificada

def greeting():
    return 'Welcome to python'

def uppercase_decorator(function):
    def wrapper():
        func = function() #ejecuta la funcion original, 'greeting'
        make_uppercase = func.upper() #modifica el resultado pasandolo a mayusculas
        return make_uppercase
    return wrapper #devuelve la funcion envolvente sin ejecutarla
g = uppercase_decorator(greeting)
print(g())

#aceptacion de parametros en funciones decoradas
def decorator_with_parameters(function): #va a recibir la funcion print_full_name
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("Yo vivo en: {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters #python reasigna automaticamente la funcion
def print_full_name(first_name, last_name, country):
    print("Yo soy {} {}. Me gusta aprender. ".format(first_name, last_name))
print_full_name("Jossie","Diaz","Colombia")