#LIMPAR TELA 
import os
os. system("Cls || clear")

#DECLARANDO AS VARIAS 
nome = str (input("Digite o seu nome: "))
n1 = int (input ("Digite o seu primeiro numero: "))
n2 = int (input("Digite o seu segundo numero: "))
maiorNum = 0
menorNum = 99999999999

#FAZENDO AS OPERAÇÕES
soma = n1 + n2
produto = n1 * n2
media = soma / 2

#CASO SEJAM IGUAIS
if n1 == n2:
   iguais = "São iguais"

#COMPARANDO OS VALORES
if maiorNum < n1:
    maiorNum = n1

if maiorNum < n2:
    maiorNum = n1

if menorNum > n1:
    menorNum = n2

if menorNum > n2:
    menorNum = n2

#MOSTRANDOS OS RESULTADOS
print (media)
print (produto)
print (f"O seu Menor numero: {n1}")
print (f"O seu Maior numero: {n2}")
print (iguais)
