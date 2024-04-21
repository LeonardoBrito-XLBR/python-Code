# Função para verificar se um número é inteiro, positivo e par
def validar_numero(numero):
    return numero.isdigit() and int(numero) % 2 == 0 and int(numero) > 0

# Lista para armazenar os valores
valores = []

# Loop para obter os 6 valores
while len(valores) < 6:
    valor = input("Digite um número inteiro, positivo e par: ")
    if validar_numero(valor):
        valores.append(int(valor))
    else:
        print("O valor informado não atende aos critérios. Tente novamente.")

# Mostrar os valores lidos na ordem inversa
print("Valores lidos na ordem inversa:")
for valor in reversed(valores):
    print(valor)