import random
import os
os.system("cls")

class Canditado: 
    def __init__(self, nome, idade, partido, votos):
        self.nome = nome
        self.idade = idade
        self.partido = partido
        self.votos = votos
    
    def __str__(self):
        return f"Nome: {self.nome} Partido: {self.partido} Votos: {self.votos}"

#FUNCAO CADASTRANDO CADA CANDIDATO 
def cadastrarCandidatos():
    nome = input("Digite o seu nome sr(a): ")
    idade = int(input("Digite sua idade: "))
    
    while True:
        partido = (input("Digite o seu partido (5 numeros): "))
        
        #VALIDAÇÃO DE NUMERO DO PARTIDO
        if len(partido) >= 6 or len(partido) <= 4:
            print("Impossivel cadastrar esse candidato!")
        else:
            print("Partido reconhecido no sistema!")
            break
            
    #RECEBENDO A QUANTIDADE DE VOTOS ALEATORIAMENTE
    votos = votosAleatorios()
        
    #ENVINADO PARA O CLASS
    candidato = Canditado(nome, idade, partido, votos)   
    return candidato 


#FUNCAO PARA RECEBER OS NUMEROS DE VOTOS 
def votosAleatorios():
    quantVotos = random.randint(3,15)
    return quantVotos


# FUNCAO PARA VER O RESULTADO
def resultadoVotacao(candidatos):
    maiorVoto = candidatos[0]
    
    for cand in candidatos:
        if cand > maiorVoto:
            maiorVoto = cand

    return maiorVoto

#ARRAY DE CANDIDATOS
conjCandidatos = []

#ADICIIONANDO CADA OBJETO NO ARRAY 
for i in range(3):
    pessoa = cadastrarCandidatos()
    conjCandidatos.append(pessoa)
    os.system("cls")

for c in conjCandidatos:
    print(c)

resulatdo = resultadoVotacao(conjCandidatos)
print(resulatdo)