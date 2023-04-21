"""
Python define tres tipos de datos num�ricos b�sicos: enteros, n�meros de punto flotante (simular�a el conjunto de los n�meros reales, pero ya veremos que no es as� del todo) y los n�meros complejos.
"""

"""
N�meros enteros
El tipo de los n�meros enteros es int. 
"""

>>> a = -1  # a es de tipo int y su valor es -1
>>> b = a + 2  # b es de tipo int y su valor es 1
>>> print(b)
1

"""
Los n�meros octales se crean anteponiendo 0o a una secuencia de d�gitos octales (del 0 al 7).

Para crear un n�mero entero en hexadecimal, hay que anteponer 0x a una secuencia de d�gitos en hexadecimal (del 0 al 9 y de la A la F).

En cuanto a los n�meros en binario, se antepone 0b a una secuencia de d�gitos en binario (0 y 1).
"""

>>> diez = 10
>>> diez_binario = 0b1010
>>> diez_octal = 0o12
>>> diez_hex = 0xa
>>> print(diez)
10
>>> print(diez_binario)
10
>>> print(diez_octal)
10
>>> print(diez_hex)
10

