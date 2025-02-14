import os
import time
os.system("cls")

#VETORES PRE-DEFINIDOS
numeros = []
numerosNegativos = []
numerosPositivos = []

#MENSAGEM 

print("DIGITE '0' PARA NÃO LER NENHUM NUMERO! ")

time.sleep(3)
#CAPTURANDO OS NUMEROS
for num in range(10):
    num = int(input("Digite o NUMERO: "))
    
    if num != 0:
        
        numeros.append(num)
    
    #VERIFICACAO
    if num > 0 and num != 0:
        numerosPositivos.append(num)

    elif num < 0 and num !=0:
        numerosNegativos.append(num)
        
        
#QUANTIDADES DE NUMEROS 
quantNum = len(numeros)
quantNegativos = len(numerosNegativos)
quantPositivos = len(numerosPositivos)

somaPositivos = sum(numerosPositivos)
somaNegativos = sum(numerosNegativos)


os.system("cls")
#EXIBIÇÃO DOS DADOS
print(f"A QUANTIDADE TOTAL DOS NUMEROS INSERIDOS: {quantNum}")
print(f"A QUANTIDADE DE NUMEROS POSITIVOS: {quantPositivos}")
print(f"A QUANTIDADE DE NUMEROS NEGATIVOS: {quantNegativos}")
print(f"NUMEROS NEGATIVOS INSERIDOS: {numerosNegativos}")
print(f"NUMEROS POSITIVOS INSERIDOS: {numerosPositivos}")
print(f"SOMA DOS NUMEROS POSITIVOS: {somaPositivos}")
print(f"SOMA DOS NUMEROS POSITIVOS: {somaNegativos}")

time.sleep(5)

print(f"\nOS NUMEROS INSERIDOS: {numeros}")



