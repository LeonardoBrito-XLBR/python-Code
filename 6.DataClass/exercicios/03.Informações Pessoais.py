# Criar um sistema de Biblioteca com 4 funcionalidades
# FAZER UM LAÇO PARA SAIR E ENTRA NOS COMANDOS

'''
resultado  = (numLidas / numTotal ) * 100
print (f"Então vc leu cerca de {resultado:.2f}% do seu livro")

'''
import os
import time
os.system("Cls || clear")
# Limpar o console
def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

# Classe para o usuário
class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

# Função para exibir a tabela principal
def exibir_tabela_principal():
    print("CÓDIGO  -  DESCRIÇÃO")
    print("#1 \t-  Cadastro de Usuário")
    print("#2 \t-  Compra de Livro")
    print("#3 \t-  Empréstimo ou Devolução")
    print("#4 \t-  Cadastro de Livro")
    print("#0 \t-  Sair")
    print("-"*35)

    try:
        opcao = int(input("Digite a sua opção: "))
        return opcao
    except ValueError:
        print("Erro: A opção deve ser um valor numérico inteiro.")
        return None

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite o seu nome completo: ")
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    return Usuario(nome, login, senha)

# Função para fazer login e retornar o usuário correspondente
def fazer_login(usuarios_cadastrados):
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    for usuario in usuarios_cadastrados:
        if usuario.login == login and usuario.senha == senha:
            return usuario

    print("Login ou senha incorretos.")
    return None

# Função para exibir a tabela de compras
def exibir_tabela_compras():
    print("CÓDIGO   - \tLIVRO \t\t - \t\tPREÇO")
    print("#1\t - Caminhos do Destino   - \tR$15 ")
    print("#2\t - Além das Estrelas     - \tR$20 ")
    print("#3\t - Entre o Sol e a Lua   - \tR$25 ")
    print("#4\t - A Sombra do Passado   - \tR$30 ")
    print("#5\t - O Poder da Imaginação - \tR$35 ")

# Função principal para o programa da biblioteca
def programa_biblioteca():
    usuarios = []  # Lista para armazenar os usuários cadastrados

    while True:
        limpar_console()
        opcao = exibir_tabela_principal()

        if opcao == 1:
            limpar_console()
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso!")
            time.sleep(2)

        elif opcao == 2:
            limpar_console()
            usuario_logado = fazer_login(usuarios)
            if usuario_logado:
                exibir_tabela_compras()
                # Aqui você pode implementar a lógica para compra de livros
                input("Pressione Enter para continuar...")
        
        elif opcao == 3:
            limpar_console()
            usuario_logado = fazer_login(usuarios)
            if usuario_logado:
                # Implementar lógica para empréstimo ou devolução de livros
                print("Empréstimo ou devolução de livros.")
                input("Pressione Enter para continuar...")
        
        elif opcao == 4:
            limpar_console()
            usuario_logado = fazer_login(usuarios)
            if usuario_logado:
                # Implementar lógica para cadastro de livros
                print("Cadastro de livros.")
                input("Pressione Enter para continuar...")
        
        elif opcao == 0:
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Digite um número válido.")

# Executar o programa principal
programa_biblioteca()

            
# ====================================================================
'''
# EXERCICIO 3 - PORCENTAGEM DE LEITURA
import os

import time


numTotal = int (input ("Quantas paginas tem esse livro? "))

numLidas = int (input ("Quantas paginas você já leu? "))

resultado  = (numLidas / numTotal ) * 100

print (f"Então vc leu cerca de {resultado:.2f}% do seu livro")'''
