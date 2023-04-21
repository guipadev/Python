'''
Escribe una funci�n llamada promedio que reciba una lista de n�meros y retorne el promedio:

# escribe la funci�n promedio

# c�digo de prueba
print(promedio([1, 2, 3])) # 2
print(promedio([8, 4, 7, 9])) # 7
print(promedio([])) # 0
'''

def promedio(lista):
    suma = sum(lista)
    if suma > 0:
        return(suma // len(lista))
    else:
        return suma

print(promedio([1, 2, 3])) # 2
print(promedio([8, 4, 7, 9])) # 7
print(promedio([])) # 0