import os
'''
def operação (n1,n2):
    soma = n1 + n2
    substrair = n1 - n2
    multiplica = n1 * n2
    division = n1 / n2
    resultado = soma, substrair, multiplica, division
    return resultado


numero1 = int (input ("Digite o seu numero: "))
numero2 = int (input ("Digite o seu numero: "))

total = operação (numero1, numero2)
os. system ("cls || clear")
print (total)
'''

def somar (n1, n2):
    resultado = n1 + n2
    return resultado

def substrair (n1, n2):
    return n1 - n2

def multiplica(n1, n2):
    return  n1 * n2

def division (n1, n2):
    return n1 / n2


num1 = int (input ('Digite o seu numero: '))
num2 = int (input ('Digite o seu numero: '))

soma=somar (num1,num2)
subtracao=substrair (num1,num2)
multiplicacao=multiplica (num1,num2)
divisao=division (num1,num2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Divisao: {divisao}")