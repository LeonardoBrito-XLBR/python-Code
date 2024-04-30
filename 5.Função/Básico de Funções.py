os. system ('cls || clear ')
import os

#TUDO SOBRE FUNÇÃO NESSE ARTIGO



# 1º EXEMPLO = IMPRIMINDO ALGUM TEXTO


#crinado a função
def saudações ():
    print ('Olá Mundo')

#chamando
saudações ()


#COMO MAIS DE UM TEXTO
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

#QUER APAGAR QUANDO APARECER A FUNÇÃO?
def logo ():
    os.system("cls || clear")
    print ("Apagando...")

logo ()