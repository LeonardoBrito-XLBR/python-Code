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
for i in range (2):

    #PREENCHENDO A CLASS COM CADA ATRIBUTO
    pessoa = Usuario(
    nome =  input ("Digite  o seu nome: "), # NÃO ESQUEÇA DA VIRGULA
    idade = int (input ("Digite a sua idade: ")),
    peso = float (input("Digite o seu peso: ")),
    
    )
    print () # <= \n
    #LISTA  >  RECEBE >  VARIAVEIS
    listaUsuarios.append(pessoa)


#CRIANDO O ARQUIVO.TXT
arquivo = "Usuarios.txt"

                      # as = apelidando
with open(arquivo, "w") as arquivoUsuarios:

    #write = escreva
    arquivoUsuarios.write ("=== DADOS DO USUARIO === \n")

    #laço para exibir cada item na lista
    for usu in listaUsuarios:
        #o arquivo apelidado vai escrever tal coisa
        arquivoUsuarios.write(f"\nSeu nome é: {usu.nome}\nSua idade:{usu.idade}\nSeu peso:{usu.peso}\n")
        #variavel onde vai buscar na class oq 

#LENDO O ARQUIVO.txt
with open(arquivo, "r") as arquivoLendo:
    leituraArquivo = arquivoLendo.read()

os.system("cls || clear")
print(f"{leituraArquivo}\n")

        