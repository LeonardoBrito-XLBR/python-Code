import os
os. system ("cls || clear")

soma: float = 0

for i in range (3):
    nota = float(input(f'Digite a sua {i + 1}ª nota: '))

    while (nota  < 0 or nota > 10):
        print ('ERRO ESCREVA UM NUMERO ENTRE 0 E 10 ')
        nota =  float(input(f'Tente de novo - Digite a sua {i + 1} nota: '))

    if nota >= 0 and nota <= 10:
        soma += nota


media = soma / 3

print ('A sua media: ', media)