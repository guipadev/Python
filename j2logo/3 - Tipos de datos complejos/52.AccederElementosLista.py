"""
Para acceder a un elemento de una lista se utilizan los �ndices. Un �ndice es un n�mero entero que indica la posici�n de un elemento en una lista. El primer elemento de una lista siempre comienza en el �ndice 0.
"""

>>> lista = ['a', 'b', 'd', 'i', 'j']
>>> lista[0]  # Primer elemento de la lista. �ndice 0
'a'
>>> lista[3]  # Cuarto elemento de la lista. �ndice 3
'i'

"""
Si se intenta acceder a un �ndice que est� fuera del rango de la lista, el int�rprete lanzar� la excepci�n IndexError. De igual modo, si se utiliza un �ndice que no es un n�mero entero, se lanzar� la excepci�n TypeError:
"""

>>> lista = [1, 2, 3]  # Los �ndices v�lidos son 0, 1 y 2
>>> lista[8]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range

>>> lista[1.0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: list indices must be integers or slices, not float


"""
Como hemos visto, las listas pueden contener otros elementos de tipo secuencia de forma anidada. Por ejemplo, una lista que uno de sus �tems es otra lista. Del mismo modo, se puede acceder a los elementos de estos tipos usando �ndices compuestos o anidados:
"""

>>> lista = ['a', ['d', 'b'], 'z']
>>> lista[1][1]  # lista[1] hace referencia a la lista anidada
'b'