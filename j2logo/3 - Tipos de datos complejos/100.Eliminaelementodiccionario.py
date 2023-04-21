"""
En Python existen diversos modos de eliminar un elemento de un diccionario. Son los siguientes:

pop(clave [, valor por defecto]): Si la clave est� en el diccionario, elimina el elemento y devuelve su valor; si no, devuelve el valor por defecto. Si no se proporciona el valor por defecto y la clave no est� en el diccionario, se lanza la excepci�n KeyError.
popitem(): Elimina el �ltimo par clave: valor del diccionario y lo devuelve. Si el diccionario est� vac�o se lanza la excepci�n KeyError. (NOTA: En versiones anteriores a Python 3.7, se elimina/devuelve un par aleatorio, no se garantiza que sea el �ltimo).
del d[clave]: Elimina el par clave: valor. Si no existe la clave, se lanza la excepci�n KeyError.
clear(): Borra todos los pares clave: valor del diccionario.
"""

>>> d = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}

# Elimina un elemento con pop()
>>> d.pop('uno')
1
>>> d
{'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}

# Trata de eliminar una clave con pop() que no existe
>>> d.pop(6)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 6

# Elimina un elemento con popitem()
>>> d.popitem()
('cinco', 5)
>>> d
{'dos': 2, 'tres': 3, 'cuatro': 4}

# Elimina un elemento con del
>>> del d['tres']
>>> d
{'dos': 2, 'cuatro': 4}

# Trata de eliminar una clave con del que no existe
>>> del d['seis']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'seis'

# Borra todos los elementos del diccionario
>>> d.clear()
>>> d
{}