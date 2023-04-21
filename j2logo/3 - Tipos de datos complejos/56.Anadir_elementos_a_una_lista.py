"""
Tal y como te he adelantado, las listas son secuencias mutables, es decir, sus elementos pueden ser modificados (se pueden a�adir nuevos �tems, actualizar o eliminar).

Para a�adir un nuevo elemento a una lista se utiliza el m�todo append() y para a�adir varios elementos, el m�todo extend():
"""

>>> vocales = ['a']
>>> vocales.append('e')  # A�ade un elemento
>>> vocales
['a', 'e']


>>> vocales.extend(['i', 'o', 'u'])  # A�ade un grupo de elementos
>>> vocales
['a', 'e', 'i', 'o', 'u']


# Tambi�n es posible utilizar el operador de concatenaci�n + para unir dos listas
# en una sola. El resultado es una nueva lista con los elementos de ambas:

>>> lista_1 = [1, 2, 3]
>>> lista_2 = [4, 5, 6]
>>> nueva_lista = lista_1 + lista_2
>>> nueva_lista
[1, 2, 3, 4, 5, 6]

# Por otro lado, el operador * repite el contenido de una lista n veces:

>>> numeros = [1, 2, 3]
>>> numeros *= 3
>>> numeros
[1, 2, 3, 1, 2, 3, 1, 2, 3]


# Tambi�n es posible a�adir un elemento en una posici�n concreta de una lista 
# con el m�todo insert(�ndice, elemento). Los elementos cuyo �ndice sea mayor 
# a �ndice se desplazan una posici�n a la derecha:

>>> vocales = ['a', 'e', 'u']
>>> vocales.insert(2, 'i')
>>> vocales
['a', 'e', 'i', 'u']












