import os
import time
import random
os.system("cls || clear")


lista = []

x =0

for i in range(5):
    
    nome = input(f"Digite o {x + 1}ªnome: ")
    x +=1
    
    lista.append(nome)
    
num = random.choice(lista)

print(num)

    