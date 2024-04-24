import os
os.system("cls" if os.name == "nt" else "clear")

#CONSERTA QUANDO PARA NO 0


# CRIANDO UM VETOR
vetor = []
i: int = 0
soma: int = 0
quant: int = 0


#COMPARAÇÃO
maiorNum = 0
menorNum = 999999



# ENTRADA DOS DADOS
while True:
    i += 1

    numero = int(input(f"Digite o seu { i }ª numero: "))
    vetor.append(numero)

# ESPAÇO PARA AS DEF
    def QuantidadePares(vetor):
        pares = 0
        for num in vetor:
            if num % 2 == 0 and num != 0:
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
    mediaImpares: float = 0
    for numero in vetor:
        if numero % 2 != 0:
            somaImpares += numero
            mediaImpares = somaImpares / Impares

    somaPositivo: int = 0
    for numero in vetor:
        if numero > 0:
            somaPositivo += numero
            mediaPositive = somaPositivo / Positivo
        

    somaNegative: int = 0
    for numero in vetor:
        if numero < 0:
            somaNegative += numero
            mediaNegative = somaNegative / Negativo
        else:
           mediaNegative = 'Nenhum valor negativo digitado'

    #MEDIA GERAL DOS NUMEROS
    if numero != 0:
        soma += numero
        quant += numero
        media = soma / quant

    #MAIOR E MENOR NUMERO
    if numero > maiorNum:
        maiorNum = numero
    
    if numero < menorNum and numero != 0:
        menorNum = numero

    #STOP LOOP
    if numero == 0:
        break

# SAÍDA DOS DADOS

os. system ('cls || clear')
for i in reversed(vetor):
    print(f'O seus {i}ª número foi: {i}')

print(f"Quantidade de números pares: {Pares}")
print (f'Quantidade de números impares {Impares}')
print (f'Quantidade de números positivos {Positivo}')
print (f'Quantidade de números negativos {Negativo}')
print (f'Média geral dos números: {media}')


print (f'Média dos Pares: {mediaPares}')
print (f'Média dos Impares: {mediaImpares}')
print (f'Média dos Positivos: {mediaPositive}')
print (f'Média dos Negativos: {mediaNegative}')

print (f'Maior número: {maiorNum}')
print (f'Menor número: {menorNum}')