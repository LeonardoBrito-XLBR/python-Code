import os 
import random


#REGRA PARA O DESAFIO: DESCOBRIR POSSIVEIS SENHAS 
# NUMERO MAX = 4 DIGITIOS 
# O PRIMEIRO DEVE SER MAIOR QUE O ULTIMO
# A SOMA PRECISA  DA 20 
# NAO PODE SE REPETIR NUMEROS 


os.system("cls")    

#FUNCAO PARA VERIFICAR O NUMERO MAXIMO DE DIGITADOS 
def Contar_Digitos(senha):
    
    quantidade = 0
    
    for i in senha:
        quantidade += 1 
    

    if quantidade > 4: 
        return False
    else:
        return True

# FUNCAO PARA VERIFICAR SE PRIMERO NUM > ULTIMO NUM 
def Maior_Ultimo(senha):
    if senha[0] > senha[3]:
        return True
    else:
        return False

# FUNCAO PARA VERIFICAR A SOMA DOS NUMERO 
def Somar_Senha(senha):
    soma = 0
    
    for i in senha:
        soma += i 
        
    if soma > 20 or soma < 20: 
        return False 
    else:
        return True
    
# VERIFICAR SE O NUMERO E IGUAL 
def Repetir_Numeros(senha):   
    
    vistos = []
    
    for numero in senha:
        if numero in vistos:
            print(f"SENHA INVALIDA [NUMERO REPETIDO]: {numero}")
            return False
        elif numero not in vistos:
            vistos.append(numero)
    

    return True


# ======= PRINCIPAL PROGRAMA ======== 
validador = True

contador = 0

#LOOP PARA TENTAR ATE ACERTAR 
senhasValidas = []
while len(senhasValidas) < 3:
    print("")
    
    # SENHA VAZIA PARA CADA TENTATIVA
    senha = []
    
    # ISSO AQUI GERAR 4 DIGITIOS E ADICIONAR NO ARRAY 
    for i in range(4):
        num = random.randint(0,9)
        senha.append(num)

    print(f" TESTANDO A SENHA: {senha}")     


    # ===== VERIFICAÇÃO DAS 4 PARTES ======
    validador = (Contar_Digitos(senha))
    if validador == False:
        print("SENHA INVALIDA: QUANTIDADE INCORRETA DE NUMEROS")
        continue
    else:
        print("SENHA CORRETA: QUANTIDADE DE NUMERO CORRETA")
        contador += 1
    

    validador = (Maior_Ultimo(senha))
    if validador == False:
        print("SENHA INVALIDA: PRIMEIRO < ULTIMO NUMERO")
        continue 
    else:
        print("SENHA CORRETA: O PRIMEIRO NUMERO > ULTIMO")
        contador += 1
    
    
    validador = (Somar_Senha(senha))
    if validador == False:
        print(f"SENHA INVALIDA: SOMA NÃO DÁ [20]")
        continue 
    else:
        print ("SENHA CORRETA: SOMA É IGUAL A [20]")
        contador += 1


    validador = (Repetir_Numeros(senha))
    if validador == False:
        print("SENHA INVALIDA: NUMEROS REPETIDOS INDENTIFICADOS")
        continue  
    else:
        print("SENHA CORRETA: NENHUM NUMERO REPETIDO INDENTIDICADO")
        contador += 1
    
    # VERIFICA SE A SENHA JÁ FOI ENCONTRADA ANTES (PARA EVITAR DUPLICATAS)
    if senha in senhasValidas:
        print("SENHA JÁ ENCONTRADA ANTES, IGNORANDO...")
        continue
    
    print("")
    print(f"✅ SENHA ACEITA COM SUCESSSO {senha}")
    print(f"🔥 NUMERO DE TENTATIVAS: {contador}")
    
    senhasValidas.append(senha.copy())  # ADICIONA UMA COPIA PARA EVITAR REFERENCIAS COMPARTILHADAS


print("")
print("SENHAS VALIDAS ENCONTRADAS: ")
for i, senha in enumerate(senhasValidas, start=1):
    print(f"Senha {i}: {senha}")  # Exibe cada senha com um índice para clareza