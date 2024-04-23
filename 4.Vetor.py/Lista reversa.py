import os
os.system('cls || clear')

lista = []

while len(lista) < 6:
    num = int(input("Digite o seu numero: "))

    if num > 0 and num % 2 == 0:
        lista.append(num)
        lista_reserva = list (reversed (lista))

        os.system ("cls || clear")

for i in range(len(lista)):
    print(f'Número: {lista_reserva[i]}')


