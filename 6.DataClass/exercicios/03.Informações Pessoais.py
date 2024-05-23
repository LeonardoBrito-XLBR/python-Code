import os
from dataclasses import dataclass

os.system('cls || clear')

conjuntoDados = []

@dataclass
class Usuario:
    nome: str
    dataNascimento: str
    rg: int
    cpf: int

def SolicitandoDados (conjuntoDados):
    funcionario = Usuario(
        nome = input ("Digite o seu nome: "),
        dataNascimento = input ("Digite o sua data de nascimento: "),
        rg = input ("Digite o seu RG: "),
        cpf = input ("Digite o seu CPF: ")
    )
    conjuntoDados.append(funcionario)
'''
TERMINAR EM CASA LEO - _ - 
'''


def Salvar():
    with open("Funcionarios.txt", "w", encoding="utf-8")as arquivo:
        for funcionario in conjuntoDados:
            arquivo.write(f"Nome:{funcionario.nome}")