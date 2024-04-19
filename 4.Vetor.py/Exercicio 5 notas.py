import os 
os. system ("cls || clear")

numeros = []

for i in range (5):
    num: int = (input (f"Digite a sua {i + 1} nota: "))
    numeros.append (num)

maiorNumero = max(numeros)
menorNumero = min (numeros)

os. system ("cls || clear")
print (f'Maior numero: {maiorNumero}')
print (f'Menor numero: {menorNumero}')

for i in range (len (numeros)):
    print (f'\n{i + 1}º numero: {numeros[i]}')