import os
from dataclasses import dataclass

os.system('cls || clear')

#CRIANDO LISTA PARA GUARDA OS 5 FUNCIONÁRIOS
conjuntoDados = []

#CRIANDO A CLASS
@dataclass
class Usuario:
    nome: str
    dataNascimento: str
    rg: int
    cpf: int

#CRIANDO FUNÇÃO PARA ENVIAR OS DADOS PARA LISTA + DANDO INFORMAÇÕES + GUARDANDO CLASS NUMA VARIAVEL(FUNCIONARIO)
def SolicitandoDados (conjuntoDados):
    for i in range(2):
        funcionario = Usuario(
            nome = input ("Digite o seu nome: "),
            dataNascimento = input ("Digite o sua data de nascimento: "),
            rg = input ("Digite o seu RG: "),
            cpf = input ("Digite o seu CPF: ")
        )
        print()
        conjuntoDados.append(funcionario)

    print ("Dados do Funcionário cadastrado!!!")

#GUARDANDO O ARQUIVO NUMA VARIAVEL
arquivo = "Funcionarios.txt"

#CRIANDO FUNÇÃO PARA CRIAR UM ARQUIVO EXTERNO 
def Salvar():
   with open(arquivo, "w", encoding="utf-8")as arquivo1:
        arquivo1.write("===== DADOS DO USUARIOS =====\n")

        for funcionario in conjuntoDados:
            arquivo1.write(f"Nome: {funcionario.nome}\nData de Nascimento: {funcionario.dataNascimento}\nRG: {funcionario.rg}\nCPF: {funcionario.cpf}\n\n")

def Leitura():
    #r de read (ler) / arqv é apelido
    with open(arquivo, "r") as arqv:
        leituraArquivo = arqv.read()
    print(leituraArquivo)

#CHAMADA DA FUNÇÃO
SolicitandoDados (conjuntoDados) #SOLICITO 
Salvar() # Salvo

Leitura() #Lendo e Imprimindo'''