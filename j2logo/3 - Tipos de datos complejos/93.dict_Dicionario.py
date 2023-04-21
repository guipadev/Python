La clase dict de Python es un tipo mapa que asocia claves a valores. A diferencia de los tipos secuenciales (list, tuple, range o str), que son indexados por un �ndice num�rico, los diccionarios son indexados por claves. Estas claves siempre deben ser de un tipo inmutable, concretamente un tipo hashable.

?? NOTA: Un objeto es hashable si tiene un valor de hash que no cambia durante todo su ciclo de vida. En principio, los objetos que son instancias de clases definidas por el usuario son hashables. Tambi�n lo son la mayor�a de tipos inmutables definidos por Python (int, float o str).

Piensa siempre en un diccionario como un contenedor de pares clave: valor, en el que la clave puede ser de cualquier tipo hashable y es �nica en el diccionario que la contiene. Generalmente, se suelen usar como claves los tipos int y str aunque, como te he dicho, cualquier tipo hashable puede ser una clave.

Las principales operaciones que se suelen realizar con diccionarios son almacenar un valor asociado a una clave y recuperar un valor a partir de una clave. Esta es la esencia de los diccionarios y es aqu� donde son realmente importantes. En un diccionario, el acceso a un elemento a partir de una clave es una operaci�n realmente r�pida, eficaz y que consume pocos recursos si lo comparamos con c�mo lo har�amos con otros tipos de datos.

Otras caracter�sticas a resaltar de los diccionarios:

Es un tipo mutable, es decir, su contenido se puede modificar despu�s de haber sido creado.
Es un tipo ordenado. Preserva el orden en que se insertan los pares clave: valor.