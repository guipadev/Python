"""
Realmente, la variable a hace referencia al objeto que representa al n�mero entero con valor 1. Si ahora creas una nueva variable b y le asignas tambi�n el valor 1, b est� haciendo referencia al mismo objeto que la variable a. En definitiva, a y b hacen referencia al mismo objeto y, por tanto, est�n asociadas a la misma direcci�n de memoria. Esto no es as� en otros lenguajes, pero esto es Python, jaja. En otros lenguajes a y b estar�an asociadas a direcciones de memoria diferentes.

Para que lo entiendas mejor te voy a presentar la funci�n id() que viene con Python. La funci�n id() devuelve un identificador �nico del objeto que se le pasa como par�metro. Este identificador es un entero el cu�l se garantiza que es �nico e inmutable durante toda la vida del objeto en memoria.
"""

# a y b hacen referencia al objeto que representa al entero 1
# Referencian a la misma direcci�n de memoria
>>> a = 1
>>> b = 1
>>> id(1)
4299329328
>>> id(a)
4299329328
>>> id(b)
4299329328

# b es asignado con el objeto que representa el entero 2
# a y b referencian a diferentes direcciones de memoria
# a mantiene la referencia al entero 1
>>> b = 2
>>> id(a)
4299329328
>>> id(b)
4299329360

# a es asignada con el valor de b
# a y b referencian al mismo objeto y, por tanto,
# a la misma direcci�n de memoria
>>> a = b
>>> id(a)
4299329360
>>> a
2