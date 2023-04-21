"""
type() recibe como par�metro un objeto y te devuelve el tipo del mismo.

isinstance() recibe dos par�metros: un objeto y un tipo. Devuelve True si el objeto es del tipo que se pasa como par�metro y False en caso contrario.
"""

>>> type(3)
<class 'int'>

>>> type(2.78)
<class 'float'>

>>> type('Hola')
<class 'str'>

>>> isinstance(3, float)
False

>>> isinstance(3, int)
True

>>> isinstance(3, bool)
False

>>> isinstance(False, bool)
True