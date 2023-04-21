'''
Escribe una funci�n crear_rango que reciba un n�mero y retorne una lista desde 1 hasta el n�mero recibido. Si el n�mero es menor a 1 retorna un lista vac�a.

# escribe la funci�n crear_rango ac�

# c�digo de prueba
print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # []
'''

def crear_rango(numero):
    
    if numero < 1:

        return []

    else:
        
        return list(range(1, numero + 1))

print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # []