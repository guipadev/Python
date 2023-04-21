'''
Escribe una funci�n llamada multiplicar que reciba un lista y un n�mero. La funci�n debe retornar una nueva lista con todos los elementos multiplicados por el n�mero:

# escribe la funci�n multiplicar

# c�digo de prueba
print(multiplicar([1, 2, 3], 5)) # [1, 10, 15]
print(multiplicar([8, 4, 7, 9], 2)) # [16, 8, 14, 18]
print(multiplicar([])) # []

Nota: Utiliza list comprenhensions para solucionar este ejercicio.
'''

def multiplicar(lista, numero=1):
    return [multiplicador * numero for multiplicador in lista]

print(multiplicar([1, 2, 3], 5)) # [5, 10, 15]
print(multiplicar([8, 4, 7, 9], 2)) # [16, 8, 14, 18]
print(multiplicar([])) # []