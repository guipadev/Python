"""
Imagina que tienes una variable edad de tipo string cuyo valor es '25'. Se podr�a decir que edad, aunque realmente es una cadena de caracteres, contiene un n�mero. Sin embargo, si intentas sumar 10 a edad, el int�rprete te dar� un error porque edad es de tipo str y 10 un tipo num�rico.
"""

>>> edad = '25'
>>> edad = edad + 10
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str


"""
str(): Devuelve la representaci�n en cadena de caracteres del objeto que se pasa como par�metro.
int(): Devuelve un int a partir de un n�mero o secuencia de caracteres.
float(): Devuelve un float a partir de un n�mero o secuencia de caracteres.
complex(): Devuelve un complex a partir de un n�mero o secuencia de caracteres.
"""

>>> edad = int(edad) + 10  # Convierte edad a int
>>> edad  #  edad es un int
35

>>> edad = str(edad)  # Convierte edad a str
>>> edad  # edad es un str (se muestran las '')
'35'

>>> float('18.66')  # Convierte un str a float
18.66

>>> float('hola')  # Convierte un str a float (pero no es v�lido)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: could not convert string to float: 'hola'

