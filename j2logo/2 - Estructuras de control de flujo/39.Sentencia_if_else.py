"""
Hay ocasiones en que la sentencia if b�sica no es suficiente y es necesario ejecutar un conjunto de instrucciones o sentencias cuando la condici�n se eval�a a False.
"""

if condici�n:
    bloque de c�digo (cuando condici�n se eval�a a True)
else:
    bloque de c�digo 2 (cuando condici�n se eval�a a False)

"""
Imagina que est�s implementado un programa en el que necesitas realizar la divisi�n de dos n�meros. Si divides un n�mero entre 0, el programa lanzar� un error y terminar�. Para evitar esto, podemos a�adir una sentencia if ... else... como en el ejemplo siguiente:
"""

resultado = None
x = 10
y = 2
if y > 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)

"""
El resultado del script anterior es 5.0. Si ahora actualizamos el valor de y a 0, el resultado ser�a este otro:
"""
No se puede dividir 10 entre 0