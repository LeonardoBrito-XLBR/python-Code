import os
from dataclasses import dataclass

os.system("cls || clear")

livros = []
#FUNÇÃO PARA GRAVAR OS DADOS
def Salvar ():

    arquivo = "Catalogo_Livro2.txt"

    #Realizando Comandos de escrita em um arquivo externo
    with open(arquivo,"w") as arquivoDeLivros:
        for livro in livros:
            arquivoDeLivros.write(f"{livro.nome}\n{livro.autor}\n{livro.categoria}\n{livro.preco}")

    print("Dados dos Livros salvos com sucesso!")

#FUNÇÃO PRA LER OS DADOS
def lerLivros():
    with open("Catalogo_Livro2.txt", "r")as arquivo:
        livrosCadastrados = arquivo.read()
    print(livrosCadastrados)

QUANTINDADE = 2
#CRIANDO A CLASS + ATIVIDADE 
@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float #talvez int

#GUARDANDO A CLASS NUMA VARIAVEL + ADD VALORES
for i in range (QUANTINDADE):
    livros.append(Livro (
        nome = input ("Qual o nome do livro: "),
        autor = input("Qual o nome do Autor do livro: "),
        categoria = input ("Qual a categoria vai receber: "),
        preco = float (input("Quanto ele vai valer: ")),

    ))   
    print("="*20, "\n")
#Guardando os dados em uma lista

#chamando as funções
Salvar()
lerLivros()