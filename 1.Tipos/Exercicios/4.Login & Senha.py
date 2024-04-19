#LIMPAR O TERMINAL 
import os
os. system("cls || clear")

#
loginCadastrado =  input ("Crie o seu login: ")
senhaCadastrda = input("Crie a sua senha: ")

os. system("cls || clear")
print("=== TESTE OS SEUS DADOS ===")
print()


login =  input("Digite o seu login: ")
senha =  input("Digite a sua senha: ")

#TESTANDO OS LOGINS
if loginCadastrado == login and senhaCadastrda == senha :
    print ("Seja bem vindo")
else:
    print ("Acesso Negado")