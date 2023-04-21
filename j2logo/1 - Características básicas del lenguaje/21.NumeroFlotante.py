"""
El caso es que la suma de la representaci�n en punto flotante en binario del n�mero 1,1 y de la representaci�n en punto flotante en binario del n�mero 2,2, dan como resultado 3,3000000000000003
"""

>>> 1.1 + 2.2
3.3000000000000003

"""
Puedes usar el tipo float sin problemas para representar cualquier n�mero real (siempre teniendo en cuenta que es una aproximaci�n lo m�s precisa posible). Por tanto para longitudes, pesos, frecuencias, �, en los que pr�cticamente es lo mismo 3,3 que 3,3000000000000003 el tipo float es el m�s apropiado.
"""

>>> real = 1.1 + 2.2  # real es un float
>>> print(real)
3.3000000000000003  # Representaci�n aproximada de 3.3
>>> print(f'{real:.2f}')
3.30  # real mostrando �nicamente 2 cifras decimales

"""
Al igual que los n�meros enteros, un float se crea a partir de un literal, o bien como resultado de una expresi�n o una funci�n.
"""

>>> un_real = 1.1  # El literal debe incluir el car�cter .
>>> otro_real = 1/2  # El resultado de 1/2 es un float
>>> not_cient = 1.23E3  # float con notaci�n cient�fica (1230.0)