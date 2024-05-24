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
    funcionario = Usuario(
        nome = input ("Digite o seu nome: "),
        dataNascimento = input ("Digite o sua data de nascimento: "),
        rg = input ("Digite o seu RG: "),
        cpf = input ("Digite o seu CPF: ")
    )
    conjuntoDados.append(funcionario)
    print ("Dados do Funcionário cadastrado!!!")
'''
TERMINAR EM CASA LEO - _ - 
'''
#CRIANDO FUNÇÃO PARA CRIAR UM ARQUIVO EXTERNO
def Salvar():
    with open("Funcionarios.txt", "w", encoding="utf-8")as arquivo:
        for funcionario in conjuntoDados:
            arquivo.write(f"Nome:{funcionario.nome}")


#CHAMADA DA FUNÇÃO
Salvar()
SolicitandoDados (conjuntoDados)