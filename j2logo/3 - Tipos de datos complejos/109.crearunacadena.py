"""
Crear una cadena de texto en Python es muy sencillo. Simplemente encierra una secuencia de caracteres entre comillas simples '' o dobles "".
"""

>>> s = 'Hola Pythonista'
>>> s
'Hola Pythonista'
>>> type(s)
<class 'str'>

>>> s2 = "Me gusta Python"
>>> s2
'Me gusta Python'
>>> type(s2)
<class 'str'>

"""
Si quieres o necesitas que un string ocupe m�s de una l�nea, entonces debes encerrar el texto entre tres comillas simples '''...''' o dobles """...""".
"""

>>> s = '''
... Este string
...    ocupa m�s
...     de
...  una l�nea'''

>>> s
'\nEste string\n   ocupa m�s\n    de\n una l�nea'

>>> print(s)

Este string
   ocupa m�s
    de
 una l�nea

"""
Como puedes observar, el uso de las tres comillas (simples o dobles) guarda el car�cter de fin de l�nea. Esto se puede evitar a�adiendo el car�cter \ al final de cada l�nea.
"""

>>> s = '''Este string \
...    ocupa m�s \
...     de \
...  una l�nea'''

>>> s
'Este string    ocupa m�s     de  una l�nea'

>>> print(s)
Este string    ocupa m�s     de  una l�nea

"""
?? OJO: No confundas un string multil�nea con un docstring. Un docstring es un string multil�nea que se utiliza para documentar un m�dulo, funci�n, clase o m�todo, entre otros.
"""

"""
Adem�s, dos cadenas se pueden concatenar con el operador +, o incluso repetir, usando el operador *. El resultado en ambos casos es un nuevo string.
"""

>>> hola = 'hola'
>>> s = hola + ' Pythonista'
>>> s
'hola Pythonista'

>>> s2 = hola * 3 + ' Pythonista'
>>> s2
'holaholahola Pythonista'

"""
Y para terminar esta secci�n, simplemente resaltar que dos strings literales se pueden concatenar si aparecen juntos uno tras otro.
"""

>>> s = 'Hola' ' Pythonista'
>>> s
'Hola Pythonista'

>>> s = ('Hola'
... ' Pythonista'
... ' �Te gusta Python?')
>>> s
'Hola Pythonista �Te gusta Python?'