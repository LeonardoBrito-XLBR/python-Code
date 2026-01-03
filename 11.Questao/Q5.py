import os
import time
os.system("cls || clear")

numeros = []

for num in range(10):
    num = int (input("Digite numeros: "))
    numeros.append(num)
    
    
quant = len(numeros)
soma = sum(numeros)

media = soma/ quant

print(media)
    
