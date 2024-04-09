import os
os.system("Cls || clear")

##Dados do aluno
nome = str (input("Digite o seu nome: "))
idade = int (input("DIGA - ME A SUA IDADE: "))

## Criando as variaveis para a nota
media : float
soma = 0
notas = []
i = 0

for i in range (4):
    notasInput = float(input(f'diga - me a sua {i+1}ª nota:le '))
    notas.append(notasInput)
    soma += notasInput

media = soma / 4

print (f"A sua media: {media}")