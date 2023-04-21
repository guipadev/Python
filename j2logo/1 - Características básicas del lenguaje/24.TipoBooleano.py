"""
Esta clase solo se puede instanciar con dos valores/objetos: True para representar verdadero y False para representar falso.
"""

Por defecto, cualquier objeto es considerado como verdadero con dos excepciones:

Que implemente el m�todo __bool__() y este devuelva False.
Que implem�nte el m�todo __len__() y este devuelva 0.
Adem�s, los siguientes objetos/instancias tambi�n son consideradas falsas:

None
False
El valor cero de cualquier tipo num�rico: 0, 0.0, 0j, �
Secuencias y colecciones vac�as (veremos estos tipos en otros tutoriales): '', (), [], {}, set(), range(0)