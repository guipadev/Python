"""
Este orden es el siguiente, de menos prioritario a m�s prioritario: asignaci�n; operadores booleanos; operadores de comparaci�n, identidad y pertenencia; a nivel de bits y finalmente los aritm�ticos (con el mismo orden de prioridad que en las matem�ticas).

Este orden de prioridad se puede alterar con el uso de los par�ntesis ():
"""

>>> x = 5
>>> y = 2
>>> z = x + 3 * y  # El producto tiene prioridad sobre la suma
>>> z
11
>>> z = (x + 3) * y  # Los par�ntesis tienen prioridad
>>> z
16