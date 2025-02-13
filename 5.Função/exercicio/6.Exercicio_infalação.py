import os
os.system("cls clear")



def inflação(num):
    if num < 1000:
        porcentagem = 0.1  # Apenas mantém o valor decimal
    else:
        porcentagem = 0.2

    resultado = num + (num * porcentagem)
    return resultado, porcentagem  # Retorna a porcentagem como decimal

# Entrada do usuário
salario = float(input("Digite o seu salário: "))

# Chamada da função
resultado = inflação(salario)

# Exibir resultados formatados
print(f"O seu salário sofreu uma inflação de {resultado[1] * 100:.0f}% e agora será: {resultado[0]:.2f}")
