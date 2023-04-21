"""
Es posible modificar un elemento de una lista en Python con el operador de asignaci�n =. Para ello, lo �nico que necesitas conocer es el �ndice del elemento que quieres modificar o el rango de �ndices:
"""

>>> vocales = ['o', 'o', 'o', 'o', 'u']

# Actualiza el elemento del �ndice 0
>>> vocales[0] = 'a'
>>> vocales
['a', 'o', 'o', 'o', 'u']

# Actualiza los elementos entre las posiciones 1 y 2
>>> vocales[1:3] = ['e', 'i']
>>> vocales
['a', 'e', 'i', 'o', 'u']