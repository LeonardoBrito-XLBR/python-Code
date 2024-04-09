import os
os. system("cls || clear")

#SOLITANDO OS DADOS 
n1 = int (input ("1 Numero: "))
n2 = int (input ("2 Numero: "))
resultado = int (0)

print ()
#OPERADORES
opcao = input ("Qual a operação desejada: ")

match opcao:
    case '+':
        resultado: int = n1 + n2 
    case '-':
        resultado: int = n1 - n2
    case '*':
        resultado: int = n1 * n2
    case '/':
        resultado: int = n1 / n2
    
    #EXIBINDO 
print () # PULAR ESPAÇO 
print (f"O resultado: {resultado}")
