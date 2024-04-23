import os
os. system ('cls || clear ')

#TUDO SOBRE FUNÇÃO NESSE ARTIGO



# 1º EXEMPLO = IMPRIMINDO ALGUM TEXTO


#crinado a função
def saudações ():
    print ('Olá Mundo')

#chamando
saudações ()

def inicio (nome):
    print ("Nome " + nome +"Bem Vindo" )

# 2º EXEMPLO DE OPERAÇÕES MATEMATICAS


print ('\nOperação matematica')

#criando a função e realizando as operações
def operação (n1, n2):
    soma = n1 + n2
    return soma

#criando variavel e quais numero entraram na função
resultado = operação (2,5)

#mostrano a variavel
print (f'O resultado foi: {resultado}')