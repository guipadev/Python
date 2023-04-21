# En Python se puede eliminar un elemento de una lista de varias formas.

# Con la sentencia del se puede eliminar un elemento a partir de su �ndice:

# Elimina el elemento del �ndice 1
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> del vocales[1]
>>> vocales
['a', 'i', 'o', 'u']

# Elimina los elementos con �ndices 2 y 3
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> del vocales[2:4]
>>> vocales
['a', 'e', 'u']

# Elimina todos los elementos
>>> del vocales[:]
>>> vocales
[]


"""
Adem�s de la sentencia del, podemos usar los m�todos remove() y pop([i]). remove() elimina la primera ocurrencia que se encuentre del elemento en una lista. Por su parte, pop([i]) obtiene el elemento cuyo �ndice sea igual a i y lo elimina de la lista. Si no se especifica ning�n �ndice, recupera y elimina el �ltimo elemento.
"""

>>> letras = ['a', 'b', 'k', 'a', 'v']

# Elimina la primera ocurrencia del car�cter a
>>> letras.remove('a')
>>> letras
['b', 'k', 'a', 'v']

# Obtiene y elimina el �ltimo elemento
>>> letras.pop()
'v'
>>> letras
['b', 'k', 'a']

# Finalmente, es posible eliminar todos los elementos de una 
# lista a trav�s del m�todo clear():

>>> letras = ['a', 'b', 'c']
>>> letras.clear()
>>> letras
[]

# El c�digo anterior ser�a equivalente a del letras[:].