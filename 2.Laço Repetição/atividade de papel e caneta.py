import os
os. system ("cls || clear")

'''
FAZER COM VETORES NOTAS = []
VETOR: salario.append = salarioUsuario

FAZER COM IF se for 1 valor apenas
'''

#PREDEFININFO POSSIVEIS VARIAVEIS PARA O CALCULO DE MATEMATICA 
contador: int = 0
somatotal: int = 0
quantMulhesSalario: int = 0
maiorIdade = 0
menorIdade = 9999



while True: #CONSERTA COM ELSE OU COM O 'N' na opcao

    print('REPETINDO....\n')
    print ('Codigo\t|Descrição')
    print ('1\t|Adicionar')
    print ('2\t|Exibir os Resultados')
    print ('3\t|Sair\n')

    opcao = int (input ("O que o você deseja fazer? "))

    match opcao:
        case 1:
            idade = int (input ("Qual a sua idade? "))
            sexo = input ("Qual o seu sexo? ")
            salario = float (input ("Qual o seu salario? "))
            
            contador += 1
            somatotal += salario
            mediaTotal = somatotal / contador
            
           
            #REALIZANDO AS VERIFICAÇÕES E COMPARAÇÕES DOS DADOS
            if sexo == 'F'and salario > 5.000:
                quantMulhesSalario += 1
            
            if idade > maiorIdade:
                maiorIdade = idade
            
            if idade < menorIdade:
                menorIdade = idade

           
        case 2:
            print (contador)
            print (somatotal)
            print (mediaTotal)
            
            #FAZER UM IF para começar a comparar caso coloque +2 
            print (maiorIdade)
            print (menorIdade)
            
            print (quantMulhesSalario)
            break
        
        case 3:
            print (' === THE END ==== ')
            break