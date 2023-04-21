"""
Como te dec�a, la clase dict es mutable, por lo que se pueden a�adir, modificar y/o eliminar elementos despu�s de haber creado un objeto de este tipo.

Para a�adir un nuevo elemento a un diccionario existente, se usa el operador de asignaci�n =. A la izquierda del operador aparece el objeto diccionario con la nueva clave entre corchetes [] y a la derecha el valor que se asocia a dicha clave.
"""

>>> d = {'uno': 1, 'dos': 2}
>>> d
{'uno': 1, 'dos': 2}

# A�ade un nuevo elemento al diccionario
>>> d['tres'] = 3
>>> d
{'uno': 1, 'dos': 2, 'tres': 3}


# ?? NOTA: Si la clave ya existe en el diccionario, se actualiza su valor.

"""
Tambi�n existe el m�todo setdefault(clave[, valor]). Este m�todo devuelve el valor de la clave si ya existe y, en caso contrario, le asigna el valor que se pasa como segundo argumento. Si no se especifica este segundo argumento, por defecto es None.
"""

>>> d = {'uno': 1, 'dos': 2}
>>> d.setdefault('uno', 1.0)
1
>>> d.setdefault('tres', 3)
3
>>> d.setdefault('cuatro')
>>> d
{'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': None}