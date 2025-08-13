import os
import random
import time

#limpando o terminal 
os.system ("cls||clear")

def void():
    print("Sejam muitos bem vindos ao jogo pela sorte!")
    time.sleep(2)
    print("O conceito é o seguinte, quem fazer mais pontos ganha")
    pronto = input ("Prontos para começar? ")
    
    #garantindo que preencham a inicalização do jogo
    while pronto == "":
        print("eu não ouvir direito...")
        pronto = input ("Prontos crianças? ")
        
        if pronto != "":
            print ("OOOOHHHH") #referencia a bob espoja calça quadrada
            break

void ()

players = []


#FAZER COM UMA DEF COM SELEÇÃO DE 1 2 OU 3 NO TECLADO
#quantidade_play = int (input ("Quantos jogadores vão jogar? "))


#MUDAR DE ACORDO COM A QUANTIDADE DE USUARIOS


for i in range (2):
    nome = input (f"Digite o nome do {i+1} seu jogador: ")
    players.append(nome)
    
print ("Nomes Salvos com Sucesso!")
print(f"O player1 ({players[0]}) vai ser o par, o player2 ({players[1]}) vai ser impar. OK?")    

def inicio (players):
    print ("Vamos começa o jogo em...")
    time.sleep(2)
    for i in range (0,5,-1):
        print(i)
    print('GOOOO!')
    
#Gerando numero e atribuindo ao jogadores

while players[0] or players[1] <= 5:
    numero = random.randint (1, 10)
    if numero % 2 == 0:
        players[0] += 1
    else:
        players[1] +=1
    
