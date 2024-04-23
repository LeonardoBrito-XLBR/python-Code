import os
os. system ('cls || clear ')

#TUDO SOBRE FUNÇÃO NESSE ARTIGO

# 1º EXEMPLO

#crinado a função
def saudações ():
    print ('Olá Mundo')

#chamando
saudações ()

print ('\n===========')

# 2º EXEMPLO
print ('\nOperação matematica')

#criando a função e realizando as operações
def operação (n1, n2):
    soma = n1 + n2
    return soma

#criando variavel e quais numero entraram na função
resultado = operação (2,5)

#mostrano a variavel
print (f'O resultado foi: {resultado}')