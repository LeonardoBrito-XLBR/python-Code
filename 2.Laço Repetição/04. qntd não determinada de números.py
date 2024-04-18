import os
os.system ("cls || clear")

numeros: float
pares: float = 0
impares: float = 0
pares: float = 0
media = float
somapares = 0
soma = 0
contador = 0
while True:
    numeros = float (input("Digite um número: "))

    if numeros % 2 == 0:
        pares +=1
        somapares += numeros
        contador +=1
        mediaPares = somapares / contador
    else:
        impares +=1
        
    if numeros == 0:
        break

    soma += numeros

print ("Quantidade pares {pares - 1}")
print ("Quantidade de impares {impares}")