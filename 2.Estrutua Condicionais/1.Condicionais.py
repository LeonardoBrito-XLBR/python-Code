import os
os.system("cls || clear")

idade = int (input ("Digite a sua idade: "))

if idade < 18 or idade >= 45:
    print("Pode votar")
else: 
    print("NÃO pode votar")


print ("=== FIM ===")