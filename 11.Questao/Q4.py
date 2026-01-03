import os
import time
os.system("cls || clear")


nomes = []

for n in range(5):
    n = input("Digite nomes: ")
    nomes.append(n)
    
nomes.sort()
print(nomes)