import os


'''
MODO DOUGLAS 


def porcentagem (produto):

    if produto < 100:
        return produto + (produto * (10/100))
    return produto - (produto * 10/100)

os.system ("cls || clear")
preco = int (input ("Digite o seu numero: "))

final = porcentagem (preco)


print (final)

'''


def inflação (num):
    if num < 100:
        porcentagem = num * 0.1
        resultado = num + porcentagem
        return resultado
    else:
        porcentagem = num * 0.2
        resultado = num + porcentagem
        return resultado
    
#terminar em casa = 30/04/2024 > 16:43
#prof Cal :>
