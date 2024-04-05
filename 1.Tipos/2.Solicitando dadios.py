import os
# limpa o terminal
os.system("clear || cls");

# solicitando dados para o usuario

nome = input ("Qual o seu nome: ")
idade = int (input ("Digite a sua idade: "))
peso = float (input ("Digite o seu peso: "))
email = input ("Digite o seu email:")

#Exibindo os dados da pessoa
print(f"\nO seu nome: {nome}")
print(f"A sua idade: {idade}")
print(f"o seu peso foi: {peso:.2f}")
print(f"{email}@gmail.com")