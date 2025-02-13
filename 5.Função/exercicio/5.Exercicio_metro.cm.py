import os

os.system ("cls || clear")


def conversao (metro):
    resultado = metro * 100
    return resultado


num = int (input ('Digite o seu numero: '))

final = conversao (num)

print (final)