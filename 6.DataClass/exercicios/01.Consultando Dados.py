import os

#importando a biblioteca de Class
from dataclasses import dataclass

os.system ("Cls || clear")

#criando lista para cada usuario
listaUsuarios = []

#criando uma class
@dataclass
class Usuario:
    nome: str
    idade: int
    peso: float


#RECOMENDADO +++
#criando uma variavel para armazena a class 
pessoa = Usuario(
    nome =  input ("Digite  o seu nome: "), # NÃO ESQUEÇA DA VIRGULA
    idade = int (input ("Digite a sua idade: ")),
    peso = float (input("Digite o seu peso: ")),
)

#LISTA  >  RECEBE >  VARIAVEIS
listaUsuarios.append(pessoa)

#CRIANDO O ARQUIVO.TXT
arquivo = "Usuarios.txt"

# w para escrever = write || as é apelidando
with open(arquivo, "w") as arquivoUsuarios:

    #laço para exibir cada item na lista
    for usu in listaUsuarios:

        #o arquivo apelidado vai escrever tal coisa
        arquivoUsuarios.write(f"{listaUsuarios}")

#LENDO O ARQUIVO.txt
with open(arquivo, "r") as arquivoLendo:
    leituraArquivo = arquivoLendo.read()

print(leituraArquivo)

        