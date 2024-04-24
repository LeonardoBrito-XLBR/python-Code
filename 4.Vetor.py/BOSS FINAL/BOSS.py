import os
os.system("cls" if os.name == "nt" else "clear")

# CRIANDO UM VETOR
vetor = []

#COMPARAÇÃO 
maiorNum = 0
menorNum = 99999

# ENTRADA DOS DADOS
for i in range(5):
    numero = int(input("Digite o seu numero: "))
    vetor.append(numero)

# ESPAÇO PARA AS DEF
def QuantidadePares(vetor):
    pares = 0
    for num in vetor:
        if num % 2 == 0:
            pares += 1
    return pares

def QuantidadeImpares (vetor):
    impares = 0
    for num in vetor:
        if num % 2 != 0:
            impares += 1
    return impares 

def QuantidadePositivo (vetor):
    positivo = 0
    for num in vetor:
        if num > 0:
            positivo +=1
    return positivo

def QuantidadeNegative (vetor):
    negative = 0
    for num in vetor:
        if num < 0:
            negative +=1
    return negative


# RESULTADO DAS DEF
Pares = QuantidadePares(vetor)
Impares = QuantidadeImpares (vetor)
Positivo = QuantidadePositivo (vetor)
Negativo = QuantidadeNegative (vetor)

#MEDIAS DOS NUMEROS
somaPares: int = 0
for numero in vetor: #CHAMAR OS ELEMENTOS DO VETOR 
    if numero % 2 == 0:
        somaPares += numero
        mediaPares = somaPares / Pares

somaImpares: int = 0
for numero in vetor:
    if numero % 2 != 0:
        somaImpares += numero
        mediaImpares = somaImpares / Impares

somaPositivo: int = 0
for numero in vetor:
    if numero > 0:
        somaPositivo += numero
        mediaPositive = somaPositivo / Positivo

#MEDIA GERAL DOS NUMEROS
soma = sum(vetor)
quant = len(vetor)
media = soma / quant

# SAÍDA DOS DADOS
for i in reversed(vetor):
    print(f'O seu número foi: {i}')
'''
print(f"Quantidade de números pares: {Pares}")
print (f'Quantidade de números impares {Impares}')
print (f'Quantidade de números positivos {Positivo}')
print (f'Quantidade de números negativos {Negativo}')
print (f'Média geral dos números: {media}')
'''

print (mediaPares)
print (mediaImpares)
print (mediaPositive)