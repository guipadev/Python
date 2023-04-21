if cond1:
    bloque cond1 (sentencias si se eval�a la cond1 a True)
elif cond2:
    bloque cond2 (sentencias si cond1 es False pero cond2 es True)
...
else:
    bloque else (sentencias si todas las condiciones se eval�an a False)

"""
Es decir, en esta ocasi�n, se comprueba la condici�n cond1. Si se eval�a a True, se ejecuta el bloque bloque cond1 y despu�s el flujo contin�a despu�s del bloque if.

Sin embargo, si cond1 se eval�a a False, se comprueba la condici�n cond2. Si esta se eval�a a True, se ejecuta el bloque de sentencias bloque cond2. En caso contrario, pasar�a a comprobar la condici�n del siguiente elif y as� sucesivamente hasta que llegue al else, que se ejecuta si ninguna de las condiciones anteriores se evaluaron a True.

Veamos un ejemplo. Imagina que queremos comprobar si un n�mero es menor que 0, igual a 0 o mayor que 0 y en cada situaci�n debemos ejecutar un c�digo diferente. Podemos hacer uso de la estructura if � elif � else anterior:
"""
x = 28
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print('x es 0')










