import os
os. system ("cls || clear")

nota: float = -1
soma: float = 0
quantNotas = 0

print ('=== Menu ===')
print ('S   - Inserir Nota')
print ('P   - Ver quantas notas forma inseridas')
print ('N   - Calcular média arimética')

while True:
    
    resposta = input ('\nDeseja inserir uma nota: ')

    if resposta == 'S':
        nota = float (input ('Digite a sua nota: '))
        soma += nota
        quantNotas += 1

    elif resposta == 'P':

        #SE NENHUMA NOTA FOR DIGITADA        
        if quantNotas == 0:
            print ("Não foram inseridas notas. \n")
            
        #SE FOR DIGITADA
        else:
            print (f"Quantidade de notas inseridas: {quantNotas} \n")
    

    elif resposta == 'N':
        if quantNotas == 0:
            print ("Não foram inseridas notas. \n")
        else:
            break
    else:
        print ("Opção Inválida... \n")
    
media = soma / quantNotas

os. system ("cls || clear")
print (f"A sua média é igual = {media}")