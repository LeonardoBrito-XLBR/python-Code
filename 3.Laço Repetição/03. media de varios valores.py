import os
os. system ("cls || clear")

# solicitando variáveis
valores: float
media: float
contador: int = 0
soma: float = 0


while True:
    valores = float (input("Digite um valor:"))
    
    if (valores >= 0):
        soma += valores
        contador += 1
        media = soma / contador;
# BREAK = PARAR O LAÇO WHILE, OU TERMINAR QUALQUER CONDIÇÃO
    if valores < 0:
        break;

#Exibindo a media
print (f"Sua média: {media}")
