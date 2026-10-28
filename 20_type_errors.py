## Tipos de errores ##
'''
#SyntaxError
#print "hello world" #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
'''

#NameError
'''
print(age)
NameError: name 'age' is not defined
'''

#IndexError
'''
numbers = [1,2,3,4,5]
numbers[5]
IndexError: list index out of range
'''

#ModuleNotFoundError
'''
import maths
ModuleNotFoundError: No module named 'maths'
'''

#AttributeError
'''
import math
print(math.PI)
AttributeError: module 'math' has no attribute 'PI'. Did you mean '.pi' instead of '.PI'?
'''

#KeyError
'''
users = {'name':'Jossie', 'age':22, 'country':'Colombia'}
print(users['county'])
KeyError: 'county'
'''

#typeError
'''
4 + '3' -> 4 + int('3')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#ImportError
'''
from math import power -> pow
ImportError: cannot import name 'power' from 'math' (unknown location)
'''
#ValueError
'''
int('12a')
ValueError: invalid literal for int() with base 10: '12a'
'''

#zeroDivisionError
'''
1/0
ZeroDivisionError: division by zero
'''

#