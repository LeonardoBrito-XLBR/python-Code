import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float


alunos = []

while True:
    
    #ARMAZENANDO EM UMA CLASS
    aluno = Aluno (

        
        nome = input ("Digite o seu nome: "),  #<- LEMBRE- SE DA VIRGULA#
        idade = int (input("Digite a sua idade: ")),
        peso = float (input("Digite o seu peso: ")),
        altura = float (input("Digite a sua altura: "))
    )
    alunos.append(aluno)

    opcao = input ("Deseja adicionar mais um? ")

    if opcao == "não":
        break


#CRIANDO O ARQUIVO EXTERNO
arquivo = "DadosPessoais.txt"

#SOLICITANDO COMANDOS DO ARQUIVO EXTERNO
with open(arquivo, "w") as arquivoDePessoais:
    for pessoa in alunos:
        arquivoDePessoais.write(f"{pessoa.nome}\n {pessoa.idade}\n {pessoa.peso:.2f}\n {pessoa.altura:.2f}\n\n")


print ("\n\nDados salvos com Sucesso")