import os
import time
os.system("cls || clear")

#FAZER COM FUNCAO 

def somar (vetor):
    return sum(vetor)

def maior(vetor):
    return max(vetor)


numeros = []

quantNum = 10;


c = 0
for num in range(  quantNum):
    num = float (input(f"Digite um {c + 1 }ºnumero: "))
    numeros.append(num)
    
    c+=1
    
resultadoSoma = somar(numeros)
resultadoMaior = maior(numeros)


os.system("cls")
print("carregando...")
time.sleep(3)

while True:
    print("1 - PARA MOSTRAR A SOMA")
    print("2 - PARA MOSTRAR O MAXIMO")
    
    opcao = int(input("\nDigite sua opcão: "))
    
    os.system("cls")
    match opcao: 
        
        case 1: 
            print(resultadoSoma)
            
            
        case 2:
            print(resultadoMaior)
        
        case '':
            print("NADA")
    break
    