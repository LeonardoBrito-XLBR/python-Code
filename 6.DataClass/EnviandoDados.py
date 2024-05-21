import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 2

alunos = []


for i in range (QUANTIDADE_ALUNOS):
    aluno = Aluno (
        nome = input ("Digite o seu nome: "),
        idade = int (input ("Digite a sua idade: "))
    )
    alunos.append(aluno)



# Definindo arquivo para salvar os dados
# Inseridos pelo usuáridos

# nomeando os arquivos 
arquivo = "arquivo.txt"

#Percorrendo o vetor e salvando os dados por linha.

#enviando ao um arquivo externo
with open(arquivo, "w") as arquivoDeAlunos:
    for aluno in alunos:
        arquivoDeAlunos.write(f"{aluno.nome}, {aluno.idade}\n")

