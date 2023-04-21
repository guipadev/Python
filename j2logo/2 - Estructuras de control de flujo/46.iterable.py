"""
Un iterable es un objeto que se puede iterar sobre �l, es decir, que permite recorrer sus elementos uno a uno. Para ser m�s t�cnico, un objeto iterable es aqu�l que puede pasarse como par�metro de la funci�n iter().

Esta funci�n devuelve un iterador basado en el objeto iterable que se pasa como par�metro.

Finalmente, un iterador es un objeto que define un mecanismo para recorrer los elementos del iterable asociado.
"""

>>> nums = [4, 78, 9, 84]
>>> it = iter(nums)
>>> next(it)
4
>>> next(it)
78
>>> next(it)
9
>>> next(it)
84
>>> next(it)
Traceback (most recent call last):
File "<input>", line 1, in <module>
StopIteration


"""
Como puedes observar, un iterador recorre los elementos de un iterable solo hacia delante. Cada vez que se llama a la funci�n next() se recupera el siguiente valor del iterador.

En Python, los tipos principales list, tuple, dict, set o string entre otros, son iterables, por lo que podr�n ser usados en el bucle for.
"""