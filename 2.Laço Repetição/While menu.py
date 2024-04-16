import os
os. system ("cls || clear")

notas = []
contador = 1
soma: float = 0
terminar = True
nota = float ( input ("Digite a sua nota: "))

opcao = input ("\nVc quer adicionar mais um?  ")

while terminar = True: 
    match opcao:
        case 'S':
            nota = float ( input ("Digite a sua nota: "))

        case 'P':  
            print (nota)

        case 'N': 
            media = soma / contador
            print (media)
            terminar = False