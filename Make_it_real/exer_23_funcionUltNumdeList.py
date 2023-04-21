'''
Escribe una funci�n llamada ultimo que reciba una lista y retorne el �ltimo elemento. Si la lista es vac�a debe retornar "La lista est� vac�a":

# escribe la funci�n ultimo ac�

# c�digo de prueba
print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista est� vac�a"
'''

def ultimo(lista):

    if len(lista) == 0:

        return "La lista est� vac�a"

    else:

        return lista[len(lista) - 1]

print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista est� vac�a"