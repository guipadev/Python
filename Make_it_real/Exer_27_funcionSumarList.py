'''
Escribe una funci�n llamada sumar_lista que reciba una lista y retorne la suma de todos los elementos:

# escribe la funci�n sumar_lista

# c�digo de prueba
print(sumar_lista([1, 2, 3])) # 6
print(sumar_lista([5, 1, 8, 7])) # 21
print(sumar_lista([])) # 0

Nota: Este ejercicio se puede hacer con ciclos y con una funci�n incluida en Python. Intenta buscar las dos formas pero utiliza los ciclos para solucionar este ejercicio.
'''

def sumar_lista (lista_numeros):
    suma = 0
    for i in lista_numeros:
        suma += i
    return suma

# c�digo de prueba
print(sumar_lista([1, 2, 3])) # 6
print(sumar_lista([5, 1, 8, 7])) # 21
print(sumar_lista([])) # 0  