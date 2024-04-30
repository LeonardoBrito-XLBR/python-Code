import os
'''
def logo ():
    os.system ("cls || clear")
    print ("=============")
    print ("=== SENAI ===")
    print ("=============")

logo()
nome = input ('Digite o seu nome: ')

logo()
idade = int (input("digite a sua idade: "))

logo()
altura = float (input ("Digite a sua altura: "))

logo ()
print (nome, idade, altura)

'''
os.system ("cls || clear")

#CALCULANDO OS NUMEROS DIGITADOS 
def operação (n1, n2):
    resultado = n1 / n2
    return resultado

#PEDINDO OS NUMEROS
primeiroNum = int (input ("DIgite o seu numero: "))
segundoNum = int (input ("DIgite o seu numero: "))

#ENVINADO OS NUMEROS PARA A FUNÇÃO "OPERAÇÃO"
final = operação (primeiroNum, segundoNum)
#ARMAZENANDO OS DADOS DA FUNÇÃO EM UMA VARIAVEL SÓ

#MOSTRANDO O RESULTADO FINAL DA OPERAÇÃO
print (f"O resultado final: {final:.1f}")