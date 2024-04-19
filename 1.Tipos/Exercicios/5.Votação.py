import os
os. system ("clear")

nome = input ("Como vc se chama: ")
idade = int (input("Digite a sua idade: "))

if idade < 18 or idade > 65:
    print ("Você não pode votar - SAIA ")
else:
    print ("Você pode votar")