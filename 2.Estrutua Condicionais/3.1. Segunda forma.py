#limpar o terminal
import os
os.system ('cls || clear')

# criando/classificando as variavies e  solicitando os dados
nome = str  (input("Qual o seu nome? "))
idade = int  (input("Quantos anos você tem? "))
turma = (input("Qual a sua turma? "))
n1= float  (input("Digite a sua 1 nota: "))
n2= float  (input("Digite a sua 2 nota: "))
n3= float  (input("Digite a sua 3 nota: "))
n4= float  (input("Digite a sua 4 nota: "))
soma = 0 
media : float 

# fazendo o calculo para descobrir a media
soma = n1 + n2 + n3 + n4
media = soma / 4

# mostrando os dados para a pessoa
os.system("Cls || clear") #limpando a tela 

print (f"O Nome do aluno: {nome}")
print (f"A Idade do Aluno: {idade}")
print (f"A Turma do Aluno: {turma}")
print (f"A Média do aluno : {media}")
