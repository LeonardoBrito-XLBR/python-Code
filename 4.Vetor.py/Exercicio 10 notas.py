import os
os. system ('cls || clear')

numero = []
negative: int = 0
somaPositivo: int = 0
contador: int = 0

for i in range (10):
    num = int((input (f'{i + 1} - Digite o numero: ')))
    numero.append(num)

    if num < 0:
        negative +=1

    if num >= 0:
        somaPositivo += num
        contador += 1
        
os. system ("cls || clear")

for i in range (len(numero)):
    print (f'{i+1}ºNumero =  {numero[i]}')

print (f'\nA quantidade de numeros negativo: {negative}')
print (f'A soma de positivos: {somaPositivo}')

    