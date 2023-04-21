"""
La sentencia while la puedes usar en multitud de ocasiones. A continuaci�n te mostrar� un escenario t�pico de uso de bucle while: Comprobar si existe un elemento en una secuencia.

Imagina que tienes la siguiente lista de valores [5, 1, 9, 2, 7, 4] y quieres saber si el n�mero 2 est� contenido en dicha lista. La estructura t�pica de bucle while para ello es como sigue:
"""

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El n�mero 2 ha sido encontrado en el �ndice {indice}')
else:
    print('El n�mero 2 no se encuentra en la lista de valores')


"""
Como puedes observar, en el ejemplo, se utilizan 3 variables de control:

encontrado: Indica si el n�mero 2 ha sido encontrado en la lista.
indice: Contiene el �ndice del elemento de la lista valores que va a ser evaluado.
longitud: Indica el n�mero de elementos de la lista valores.
"""

"""
?? NOTA: El anterior es solo un ejemplo para que veas c�mo funciona la sentencia while. En realidad, en Python se puede usar el operador in para comprobar de forma m�s eficiente si un elemento est� contenido en una secuencia.
"""