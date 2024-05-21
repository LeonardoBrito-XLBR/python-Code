import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

# Nome do Arquivo
arquivoDeOrigem = "DadosPessoais.txt"

# Lista para Armazenar os Alunos Lidos
listaAlunos = []

# Lê os dados do arquivo
with open(arquivoDeOrigem, 'r') as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(',')
        if len(dados) == 4:
            nome, idade, peso, altura = dados
            listaAlunos.append(Aluno(nome=nome, idade=int(idade), peso=float(peso), altura=float(altura)))
        else:
            print(f"A linha '{linha.strip()}' não possui o formato esperado e será ignorada.")


#Exibir os dados lidos
print("\nExibindo Dados.")

for aluno in listaAlunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")
    print()
