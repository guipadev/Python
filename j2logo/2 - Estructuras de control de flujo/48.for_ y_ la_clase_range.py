"""
�C�mo implementamos y/o simulamos en Python el bucle for basado en una secuencia num�rica? Para estos casos, Python pone a nuestra disposici�n la clase range (en Python 2 era una funci�n). El constructor de esta clase, range(max), devuelve un iterable cuyos valores van desde 0 hasta max - 1.
"""
for i in range(11):
    print(i)

0
1
2
3
...
10


"""
El tipo de datos range se puede invocar con uno, dos e incluso tres par�metros:

range(max): Un iterable de n�meros enteros consecutivos que empieza en 0 y acaba en max - 1
range(min, max): Un iterable de n�meros enteros consecutivos que empieza en min y acaba en max - 1
range(min, max, step): Un iterable de n�meros enteros consecutivos que empieza en min acaba en max - 1 y los valores se van incrementando de step en step. Este �ltimo caso simula el bucle for con variable de control.

# Por ejemplo, para mostrar por pantalla los n�meros pares del 0 al 10
# podr�amos usar la funci�n range del siguiente modo:
"""

for num in range(0, 11, 2):
    print(num)

0
2
4
6
8
10