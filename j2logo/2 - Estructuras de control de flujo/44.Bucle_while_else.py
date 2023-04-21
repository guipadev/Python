"""
Al igual que sucede con el bucle for, podemos alterar el flujo de ejecuci�n del bucle while con las sentencias break y continue:

break se utiliza para finalizar y salir el bucle, por ejemplo, si se cumple alguna condici�n.
Por su parte, continue salta al siguiente paso de la iteraci�n, ignorando todas las sentencias que le siguen y que forman parte del bucle.
"""

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el �ndice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')

"""
Lo que he hecho ha sido eliminar de la condici�n de continuaci�n del bucle la comprobaci�n de la variable encontrado. Adem�s, he a�adido la sentencia break si el n�mero 2 se encuentra en la lista.

Por otro lado, al bucle while le podemos a�adir la sentencia opcional else. El bloque de c�digo del else se ejecutar� siempre y cuando la condici�n de la sentencia while se eval�e a False y no se haya ejecutado una sentencia break.
"""

valores = [5, 1, 9, 2, 7, 4]

indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print(f'El elemento 2 ha sido encontrado en el �ndice {indice}')
        break
    else:
        indice += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')

# En esta ocasi�n se ha eliminado completamente el uso de la 
# variable de control encontrado.