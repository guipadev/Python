'''
Escribe una funci�n llamada ordenar que reciba una lista de n�meros y retorne la lista ordenada:

# escribe la funci�n ordenar ac�

# c�digo de prueba
print(ordenar([3, 2, 1])) # [1, 2, 3]
print(ordenar([5, 1, 8, 7])) # [1, 5, 7, 8]
'''

def ordenar(lista):

    lista.sort()

    return lista


print(ordenar([3, 2, 1])) # [1, 2, 3]
print(ordenar([5, 1, 8, 7])) # [1, 5, 7, 8]