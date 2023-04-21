x = 17
if x < 20:
    print('x es menor que 20')


# Veamos otro ejemplo:


valores = [1, 3, 4, 8]
if 5 in valores:
    print('est� en valores')
print('fin')

"""
En este caso tenemos una lista de valores. El if comprueba si el n�mero 5 se encuentra entre estos valores. Como la expresi�n devuelve como resultado False, porque 5 no est� entre los valores, el c�digo anterior simplemente mostrar� por pantalla la cadena fin.

Si repetimos el ejemplo anterior, modificando la condici�n a esta otra 3 in valores, el resultado del programa ser�a:
"""

est� en valores
fin



"""
?? RECUERDA: En principio, en Python todos los objetos/instancias se eval�an a True a excepci�n de None, False, 0 de todos los tipos num�ricos y secuencias/colecciones vac�as, que se eval�an a False.
"""