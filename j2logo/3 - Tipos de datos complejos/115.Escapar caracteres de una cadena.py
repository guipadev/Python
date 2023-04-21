"""
Como un string est� limitado por los caracteres '' o "", �qu� ocurre si necesito usar el car�cter ' o " dentro de una cadena?

Lo m�s f�cil si tienes que usar el car�cter ' en tu cadena, es encerarla entre comillas dobles. Por el contrario, si necesitas usar " dentro del string, enci�rralo entre comillas simples.
"""

>>> s = 'Dijo: "Hola Pythonista"'
>>> print(s)
Dijo: "Hola Pythonista"

>>> s = "Dijo: 'Hola Pythonista'"
>>> print(s)
Dijo: 'Hola Pythonista'

"""
Tambi�n puedes usar la combinaci�n \' para mostrar una comilla simple o \" para mostrar una comilla doble, independientemente de si la cadena est� encerrada entre comillas simples o dobles.
"""

>>> s = 'Dijo: \'Hola Pythonista\''
>>> print(s)
Dijo: 'Hola Pythonista'

>>> s = "Dijo: \"Hola Pythonista\""
>>> print(s)
Dijo: "Hola Pythonista"

"""
Adem�s del car�cter ' y ", hay otros caracteres especiales que para ser usados dentro de una cadena necesitan ser �escapados� con el car�cter \. Son, entre otros, los siguientes: tabulador (\t), barra invertida (\\), retroceso (\b), nueva l�nea (\n) o retorno de carro (\r).
"""

# Ejemplo para declarar una ruta en Windows
>>> s = 'C:\\Users\\Documents\\'
>>> print(s)
C:\Users\Documents\

# Nueva l�nea m�s tabulador
>>> s = 'Hola\n\tPythonista'
>>> print(s)
Hola
  Pythonista