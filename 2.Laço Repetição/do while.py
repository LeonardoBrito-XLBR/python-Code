import os
os.system ('cls || clear')

notas = []
contador = 1
soma: float = 0

nota = float ( input ("Digite a sua nota: "))

opcao = input ("\nVc quer adicionar mais um? ")

while (opcao == "sim" ):
    nota = float ( input ("Digite a sua nota: "))

    opcao = input ("\nVc quer add mais um? ")
    
    if opcao != "sim":
        break  
    
    media = soma / notas
    print(f"Media: {media}")

    if media >= 7:
        print("APROVADO")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
    

