"""
break se utiliza para finalizar y salir el bucle, por ejemplo, si se cumple alguna condici�n.

Por su parte, continue salta al siguiente paso de la iteraci�n, ignorando todas las sentencias que le siguen y que forman parte del bucle.

Un ejemplo es la mejor manera de entenderlo.
"""

# Uso de break. Encontrar un elemento en una colecci�n

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)

# Uso de continue. Imprimir solo los n�meros pares de una colecci�n

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)

#En este caso, el c�digo anterior mostrar� los n�meros 2, 4, 8 y 4.


