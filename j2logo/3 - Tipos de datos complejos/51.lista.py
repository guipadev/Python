Las listas en Python son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos.

Junto a las clases tuple, range y str, son uno de los tipos de secuencia en Python, con la particularidad de que son mutables. Esto �ltimo quiere decir que su contenido se puede modificar despu�s de haber sido creada.

Para crear una lista en Python, simplemente hay que encerrar una secuencia de elementos separados por comas entre par�ntesis cuadrados [].

Por ejemplo, para crear una lista con los n�meros del 1 al 10 se har�a del siguiente modo:

>>> numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Como te dec�a, las listas pueden almacenar elementos de distinto tipo. La siguiente lista tambi�n es v�lida:

>>> elementos = [3, 'a', 8, 7.2, 'hola']
Incluso pueden contener otros elementos compuestos, como objetos u otras listas:

>>> lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
Las listas tambi�n se pueden crear usando el constructor de la clase, list(iterable). En este caso, el constructor crea una lista cuyos elementos son los mismos y est�n en el mismo orden que los �tems del iterable. El objeto iterable puede ser o una secuencia, un contenedor que soporte la iteraci�n o un objeto iterador.

Por ejemplo, el tipo str tambi�n es un tipo secuencia. Si pasamos un string al constructor list() crear� una lista cuyos elementos son cada uno de los caracteres de la cadena:

>>> vocales = list('aeiou')
>>> vocales
['a', 'e', 'i', 'o', 'u']
Termino esta secci�n mostrando dos alternativas de crear una lista vac�a:

>>> lista_1 = []  # Opci�n 1
>>> lista_2 = list()  # Opci�n 2