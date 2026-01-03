import os
import time
os.system("cls")

#CRIANDO OS VETORES
numeros = []

def Pause():
    return time.sleep(3)


print("O PROGRAMA VAI ENCERRA QUANDO VC DIGITAR 0")

Pause()

print("AO FINAL VAMOS EXIBIR A SOMA DELES")
Pause()


while True:
    num = int(input("\nDigite um numero: "))
    
    if num == 0:
        break
    else:
        numeros.append(num)
        
        
os.system("clear")
print(numeros)

soma = sum(numeros)

print(f"A soma de todos os numeros: {soma}")
    