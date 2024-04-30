import os
os.system ("cls || clear")

def verificar (num):
    if num % 2 == 0:
        resultado = "Par"
        return resultado 
    
    else:
        resultado = "impar"
        return resultado

numero = int (input("Digite o seu numero: "))

total = verificar (numero)

os.system ("cls || clear")
print (f"O numero verificado pelo nosso sistema é: {total}")

