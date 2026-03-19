import os 
import random


#REGRA PARA O DESAFIO: DESCOBRIR POSSIVEIS SENHAS 
# NUMERO MAX = 4 DIGITIOS 
# O PRIMEIRO DEVE SER MAIOR QUE O ULTIMO
# A SOMA PRECISA  DA 20 
# NAO PODE SE REPETIR NUMEROS 

# LISTAS = SERVEM COMO UMA VETOR DE NOMES, INT, OBJETOS, E TUDO MAIS 

    
    
#FUNCAO PARA VERIFICAR O NUMERO MAXIMO DE DIGITADOS 
def Contar_Digitos(senha):
    quantidade = 0
    
    #LOOP PARA OS CONJUNTOS NUMERICOS
    for i in senha:
        quantidade += 1 
    
    #VERIFICANDO CADA 
    if quantidade > 4: 
        print("Senha invalida: muitos numeros")
        return False
     
    elif quantidade < 4:
        print("Senha invalida: poucos numeros")
        return False
    
    else:
        print("Senha Correta")
        return True

# FUNCAO PARA VERIFICAR SE PRIMERO NUM > ULTIMO NUM 
def Maior_Ultimo(senha):
    if senha[0] > senha[3]:
        print("SENHA CORRETA" ) # STATUS DE LOG NO MAIN LOOP
        return True
    else:
        print("SENHA INVALIDA: O primeiro numero < o ultimo")
        return False

# FUNCAO PARA VERIFICAR A SOMA DOS NUMERO 
def Somar_Senha(senha):
    soma = 0
    
    for i in senha:
        soma += i
        
    if soma > 20: 
        print(f"Senha invalida: A soma dos numeros > 20 [{soma}]")
        return False 
    elif soma < 20:
        print(f"Senha invalida: A soma dos nuero < 20 [{soma}]")
        return False
    else:
        print("Senha Correta")
        return True
    
# VERIFICAR SE O NUMERO E IGUAL 
def Repetir_Numeros(senha):   
    #memoria local para comparar 
    vistos = []
    
    for numero in senha:
        
        # se o numero ja existir no array
        if numero in vistos:
            print(f"SENHA INVALIDA [NUMERO REPETIDO]: {numero}")
            return False
        elif numero not in vistos:
            # se nao existir, adicionar e comparar la em cima
            vistos.append(numero)
            # print("ADICIONADO NO ARRAY")
        else:
            print("SENHA VALIDA ")
            return True


# ======= PRINCIPAL PROGRAMA ======== 

# SENHA PARA TESTE
# senhaZ = [11,3,4,2]

validador = True
status = True

# ===== LOOP PRINCIPAL DO PROGRANA =======
senha = []

#TAL CONTADOR PARA VERIFICAR SE AS 4 VERIFICACOES FORAM ACEITAS
contador = 0

while contador != 4: 

    
    # ISSO AQUI GERAR 4 DIGITIOS E ADICIONAR NO ARRAY 
    for i in range(4):
        num = random.randint(0,9)
        senha.append(num)
        
    print(senha)      
        
    
    # ===== VERIFICAÇÃO DAS 4 PARTES ======
    validador = (Contar_Digitos(senha))
    if validador == False:
        print("ERRO AQUI VOLTANDO")
        senha = []
    else:
        contador += 1

    
    print(validador)
    validador = (Maior_Ultimo(senha))
    if validador == False:
        print("ERRO AQUI VOLTANDO")
        senha = []
    else:
        contador += 1
    
    
    print(validador)
    validador = (Somar_Senha(senha))
    if validador == False:
        print("ERRO AQUI VOLTANDO")
        senha = []
    else:
        contador += 1
    
    
    print(validador)
    validador = (Repetir_Numeros(senha))
    if validador == False:
        print("ERRO AQUI VOLTANDO")
        senha = []
    else:
        contador += 1
    
    #SE DER CERTO AQUI
print("SENHA EM FORMATO CORRETO: ")
