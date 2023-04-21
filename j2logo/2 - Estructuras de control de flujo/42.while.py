"""
el uso principal de la sentencia while es ejecutar repetidamente un bloque de c�digo mientras se cumpla una condici�n.

La estructura de esta sentencia while es la siguiente:

while condici�n:
    bloque de c�digo
Es decir, mientras condici�n se eval�e a True, se ejecutar�n las instrucciones y sentencias de bloque de c�digo.

Aqu�, condici�n puede ser un literal, el valor de una variable, el resultado de una expresi�n o el valor devuelto por una funci�n.

?? IMPORTANTE: El cuerpo del bloque while est� indicado con un sangrado mayor. Dicho bloque termina cuando se encuentre la primera l�nea con un sangrado menor.
"""

numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')


"""
En el script anterior se inicializa una variable numero con el valor 0.

Seguidamente se muestra un mensaje y en la l�nea 3 aparece una sentencia while. En esta sentencia se comprueba si el valor de la variable numero es menor o igual a 10.

Como se eval�a a True, se muestra por pantalla el resultado de multiplicar numero por 3 y despu�s se incrementa el valor de numero en 1.

A continuaci�n, se deber�a ejecutar el c�digo de la l�nea 6. Sin embargo, como hemos definido un bucle while, el flujo de ejecuci�n del programa no contin�a por la l�nea 6, sino que vuelve a la l�nea 3 y de nuevo se eval�a si la expresi�n numero <= 10 sigue siendo True. En esta ocasi�n el valor de numero es 1, por lo que la expresi�n da como resultado True y vuelven a ejecutarse las l�neas de la sentencia while.

Esto ser� as� hasta que numero sea igual a 11. En esa ocasi�n la expresi�n de comparaci�n se evaluar� a False y el flujo continuar�, ahora s�, por la l�nea 6.

El resultado del script anterior es el siguiente (la tabla de multiplicar del n�mero 3):
"""

Tabla del 3
0
3
6
9
12
15
18
21
24
27
30
Fin