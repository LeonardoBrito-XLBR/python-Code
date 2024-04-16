import os
os. system ("cls || clear")

print ('Hello World\n')

nome = input ('Digite o seu nome: ')

n1: int = (input('Digite o seu primeiro numero: '))
n2: int = (input('Digite o seu segundo numero: '))

soma = n1 + n2
substracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2
potencia = n1 ** n2
Quociente = n1 // n2

print ('\n Escolha uma opção do que vc deseja')
print ('Codigo      Resultado\n') #dois tab
print ('a       soma\n')
print ('b       substração\n')
print ('c       multiplicação\n')
print ('d       divisao\n')
print ('f       Resto da Divisão\n')
print ('g       Potência\n')
print ('h       Quociente da divisão\n')
opcao = input ('O que você quer? ')

#FAZER O IF E ELIF
while ( opcao )
    match opcao:
        case 'a':
            n1 + n2
            opcaocorreta = True
        case 'b':
            n1 - n2
            opcaocorreta =
        case 'c':
            n1 * n2
        case 'd':
            n1 / n2

        case 'e':
            n1 % n2
        
        case 'f':
            n1 ** n2
        
        case 'g':
            n1 // n2
        
        case _:
            print ('TENTE DE NOVO')
