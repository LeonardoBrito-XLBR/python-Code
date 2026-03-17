import os 
os.system("cls")

#REGRA PARA O DESAFIO: DESCOBRIR POSSIVEIS SENHAS 
# NUMERO MAX = 4 DIGITIOS 
# O PRIMEIRO DEVE SER MAIOR QUE O ULTIMO
# A SOMA PRECISA  DA 20 
# NAO PODE SE REPETIR NUMEROS 


# LISTAS = SERVEM COMO UMA VETOR DE NOMES, INT, OBJETOS, E TUDO MAIS 

        
senha = [4,2395,1,5]



#FUNCAO PARA VERIFICAR O NUMERO MAXIMO DE DIGITADOS 
def Contar_Digitos(senha):
    quantidade = 0
    
    #LOOP PARA OS CONJUNTOS NUMERICOS
    for i in senha:
        quantidade += 1 
    
    #VERIFICANDO CADA 
    if quantidade > 4 or quantidade < 4: 
        print("Senha invalida: muitos numeros")
        return False 
    else:
        return True



# FUNCAO PARA VERIFICAR SE PRIMERO NUM > ULTIMO NUM 
def Verificar_Maior_Que_Ultimo(senha):
    if senha[0] > senha[3]:
        print("O primeiro numero e maior que o ultimo" ) # STATUS DE LOG NO MAIN LOOP
        return True
    else:
        print("O primeiro numero e menor que o ultimo")
        return False
    

# FUNCAO PARA VERIFICAR A SOMA DOS NUMERO 
def Somar_Senha(senha):
    soma = 0
    
    for i in senha:
        soma += i
        
    if soma > 20: 
        print("Senha invalida: A soma dos numeros é maior que 20")
    elif soma < 20:
        print("Senha invalida: A soma dos nuero e menor que 20")
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
            print("NUMERO ERRADO")
            return False
        else:
            # se nao existir, adicionar e comparar la em cima
            vistos.append(numero)
            print("NUMERO CORRETO")
            return True
 
Repetir_Numeros(senha)


while True: 
    
    senha = [1,2,2,1,4]
    
    print (Contar_Digitos(senha))
    print(Verificar_Maior_Que_Ultimo(senha))
    print(Somar_Senha(senha))
    print(Repetir_Numeros(senha))
    
    break