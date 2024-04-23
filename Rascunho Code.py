import os
os. system ('cls || clear')

#CRIANDO O VETOR PARA RECEBER AS NOTAS
numeros = []

#CRIANDO A FUNÇÃO PRA CALCULAR AS NOTAS
def media (lista):
    soma = sum(lista)
    quant = len(lista)
    media = soma / quant
    return media

#PREENCHENDO O VETOR COM OS NUMEROS 
for i in range (3):
    num = int (input ('Digite o seu numero: '))
    numeros.append (num)

#CRIANDO UM LOCAL DO RESULTADO E ENVIANDO AS NOTAS
resultado = media (numeros)

#MOSTRANDO O LOCAL DO RESULTADO
print (f'A media foi: {resultado}')

