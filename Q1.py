import os
os.system("cls")

numbers = []


for n in range(3):
    n = int(input("Digite o seu numero: "))
    numbers.append(n)
    

maiorNum = max(numbers)

print(f" O maior numero é: {maiorNum}")    