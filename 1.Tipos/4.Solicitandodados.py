import os
os.system("cls || clear")

nome: str = (input("Digite o seu nome: "))
idade: int = (input("Digite a sua idade: "))
peso: float = (input("Digite o seu peso: "))

print(f"\no seu nome: {nome}")
print(f"a sua idade: {idade}")
print(f"o seu peso: {peso:.3f}")
