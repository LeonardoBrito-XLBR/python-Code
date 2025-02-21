import random
import os


class Canditado: 
    def __init__(self, nome, idade, partido, votos):
        self.nome = nome
        self.idade = idade
        self.partido = partido
        self.votos = votos
        
    def exibirVotos (self):
        return (f"A quantidade do {self.nome} votos foi: {self.votos}")
    
    def __str__(self):
        return f"Nome: {self.nome} Partido: {self.partido} Votos: {self.votos}"
        
def cadastrarCandidatos():
    nome = input("Digite o seu nome sr(a): ")
    idade = int(input("Digite sua idade: "))
    partido = (input("Digite o seu partido (5 numeros): "))
    
    if len(partido) > 5 or len(partido) < 5:
        print("Impossivel cadastrar esse candidato!")
        return
    else:
        print("Partido reconhecido no sistema!")
        
   
        votos = votosAleatorios()
        return Canditado(nome, idade, partido, votos)         





#FUNCAO PARA RECEBER OS NUMEROS DE VOTOS 
def votosAleatorios():
    quantVotos = random.randint(3,9)
    return quantVotos
 
 
# INICIO DO CODIGO! 

conjCanditados = []

for i in range(2):
    pessoa = cadastrarCandidatos()
    conjCanditados.append(pessoa)
    os.system("cls")
    
    
for candidato in conjCanditados:
    print(candidato) 
    

# os.system("cls")

# print("EXIBINDO AS INFORMAÇÕES")

# print(pessoa.exibirVotos())