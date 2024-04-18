import os
os. system ("cls || clear")

notas = []
contador: int = 1
soma: float = 0
terminar = True
nota = float ( input ("Digite a sua nota: "))


while True: 
    opcao = input ("\nVc quer adicionar mais um?  ")
    match opcao:
        case 'S':
            nota = float ( input ("Digite a sua nota: "))

        case 'P':  
            print (nota)
            break;

        case 'N': 
            media = soma / contador
            print (media)
            break;