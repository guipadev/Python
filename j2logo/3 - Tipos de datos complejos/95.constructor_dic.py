"""
Tambi�n se puede usar el constructor de la clase dict() de varias maneras:

Sin par�metros. Esto crear� un diccionario vac�o.

Con pares clave: valor encerrados entre llaves.

Con argumentos con nombre. El nombre del argumento ser� la clave en el diccionario. En este caso, las claves solo pueden ser identificadores v�lidos y mantienen el orden en el que se indican. No se podr�a, por ejemplo, tener n�meros enteros como claves.

Pasando un iterable. En este caso, cada elemento del iterable debe ser tambi�n un iterable con solo dos elementos. El primero se toma como clave del diccionario y el segundo como valor. Si la clave aparece varias veces, el valor que prevalece es el �ltimo.

Veamos un ejemplo con todo lo anterior. Vamos a crear el mismo diccionario de todos los modos que te he explicado:
"""

# 1. Pares clave: valor encerrados entre llaves
>>> d = {'uno': 1, 'dos': 2, 'tres': 3}
>>> d
{'uno': 1, 'dos': 2, 'tres': 3}

# 2. Argumentos con nombre
>>> d2 = dict(uno=1, dos=2, tres=3)
>>> d2
{'uno': 1, 'dos': 2, 'tres': 3}

# 3. Pares clave: valor encerrados entre llaves
>>> d3 = dict({'uno': 1, 'dos': 2, 'tres': 3})
>>> d3
{'uno': 1, 'dos': 2, 'tres': 3}

# 4. Iterable que contiene iterables con dos elementos
>>> d4 = dict([('uno', 1), ('dos', 2), ('tres', 3)])
>>> d4
{'uno': 1, 'dos': 2, 'tres': 3}

# 5. Diccionario vac�o
>>> d5 = {}
>>> d5
{}

# 6. Diccionario vac�o usando el constructor
>>> d6 = dict()
>>> d6
{}