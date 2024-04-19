import os
os. system ('cls || clear')

lista = []

while True:

    for i in range (6):
        num = int (input("Qual o numero: "))

        if num > 0 and num % 2 == 0:
            lista.append (num)
        
    for i in range (len(lista)):
        print (f'Numeros {lista}')


