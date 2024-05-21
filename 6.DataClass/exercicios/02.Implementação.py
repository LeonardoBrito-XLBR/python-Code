import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: int #talvez float

livros = []

livro = Livro (
    nome = input ("Qual o nome do livro: "),
    autor = input("Qual o nome do Autor do livro: "),
    categoria = input ("Qual a categoria vai receber: "),
    preco = int (input("Quanto ele vai receber: "))



)

#Guardando os dados em uma lista
livros.append(livro)

#Criando o arquivo Externo
arquivo = "DadosLivro.txt"

'''
TERMINAR EM CASA

'''