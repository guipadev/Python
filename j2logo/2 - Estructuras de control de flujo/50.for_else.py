for e in iterable:
    # Tu c�digo aqu�
else:
    # Este c�digo siempre se ejecuta si no
    # se ejecut� la sentencia break en el bloque for

"""
Es decir, el c�digo del bloque else se ejecutar� siempre y 
cuando no se haya ejecutado la sentencia break dentro del bloque del for.
Veamos un ejemplo:
"""
numeros = [1, 2, 4, 3, 5, 8, 6]

for n in numeros:
    if n == 3:
        break
else:
    print('No se encontr� el n�mero 3')

# Como en el ejemplo anterior la secuencia numeros contiene al n�mero 3,
# la instrucci�n print nunca se ejecutar�.