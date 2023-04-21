"""
Como el resto de tipos secuencia, podemos acceder a los caracteres de una cadena a trav�s de un �ndice num�rico. Un �ndice es un n�mero entero que indica la posici�n de un car�cter en la cadena. Siempre el primer car�cter de la secuencia tiene como �ndice 0.
"""

>>> s = 'Hola Pythonista'

# Primer car�cter de la cadena
>>> s[0]
'H'

# Sexto car�cter de la cadena
>>> s[5]
'P'

# Tercer car�cter de la cadena
>>> s[2]
'l'

"""
Si se intenta acceder a un �ndice que est� fuera del rango del string, el int�rprete lanzar� la excepci�n IndexError. De igual modo, si se utiliza un �ndice que no es un n�mero entero, se lanzar� la excepci�n TypeError
"""

>>> s = 'Hola Pythonista'

>>> s[30]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: string index out of range

>>> s[1.0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: string indices must be integers

"""
Los �ndices tambi�n puede ser negativos. En este caso, el �ndice -1 hace referencia al �ltimo car�cter, -2 al pen�ltimo, y as�, sucesivamente.
"""

>>> s = 'Hola Pythonista'
>>> s[-1]
'a'
>>> s[-2]
't'