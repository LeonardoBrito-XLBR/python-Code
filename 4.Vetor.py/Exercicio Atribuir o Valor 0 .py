import os
os. system ('cls || clear')

numeros = []

for i in range (5):
    num  = int (input ("Digite o seu numero: ") )
    numeros.append (num)

    if num < 0:
        numeros [i] = 0

for i in range (len(numeros)):
    print (f"Os numeros:  {numeros[i]}")


