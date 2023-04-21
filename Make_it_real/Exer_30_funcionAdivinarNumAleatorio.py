'''
Escribe un programa que piense un n�mero de 1 a 10 de forma aleatoria y le pida al usuario que lo trate de adivinar. El usuario puede intentar indefinidamente hasta que encuentre el n�mero.

Un ejemplo de la ejecuci�n del programa podr�a ser el siguiente, asumiendo que el n�mero es 2:

Adivina el n�mero: 5
Fallaste!

Adivina el n�mero: 2
Felicitaciones, lo encontraste!
'''

import random

def adivinar() :
  numero = random.randint(1, 10)
  while True :
    adivina = int(input("Adivina el n�mero : "))
    if numero == adivina : 
      print("Felicitaciones, lo encontraste!")
      break
    print("Fallaste!")

print("Adivina el n�mero entre 1 y 10")
adivinar()

'''
#OTRA FORMA
import random

numero = int(input("Adivina el n�mero: "))

while numero != random.randrange(1, 10):
    print("Fallaste!")
    numero = int(input("Adivina el n�mero: "))
print("Felicitaciones, lo encontraste!")
'''