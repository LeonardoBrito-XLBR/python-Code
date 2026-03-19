import random

# ===== FUNÇÕES =====

def Contar_Digitos(senha):
    return len(senha) == 4


def Maior_Ultimo(senha):
    return senha[0] > senha[3]


def Somar_Senha(senha):
    return sum(senha) == 20


def Repetir_Numeros(senha):
    return len(set(senha)) == 4


# ===== PROGRAMA PRINCIPAL =====

while True:
    # gera senha com 4 dígitos
    senha = [random.randint(0, 9) for _ in range(4)]

    print("Tentando senha:", senha)

    # REGRA 1
    if not Contar_Digitos(senha):
        print("❌ ERRO: quantidade de números inválida")
        continue

    # REGRA 2
    if not Maior_Ultimo(senha):
        print("❌ ERRO: primeiro número NÃO é maior que o último")
        continue

    # REGRA 3
    if not Somar_Senha(senha):
        print("❌ ERRO: soma diferente de 20")
        continue

    # REGRA 4
    if not Repetir_Numeros(senha):
        print("❌ ERRO: números repetidos")
        continue

    # se chegou aqui, passou em tudo
    print("✅ SENHA VÁLIDA:", senha)
    print("🔥 PASSOU PELOS 4 PARÂMETROS")
    break