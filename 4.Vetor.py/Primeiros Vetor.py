import os
os. system ("cls || clear")

#CRIANDO O VETOR
numeros = []
c: int = 0

#SOLICITANDO OS DADOS 
for i in range (5):
    nota = float (input('Digite a sua nota: '))
    numeros.append(nota)
    
media = sum(numeros) / len(numeros)

os.system ('cls || clear')

#MOSTRANDO OS DADOS
for i in range (len (numeros)):
    print (f"A nota: {i + 1}ª nota {numeros[i]}")
    c += 1
print ()

print (f'A sua media foi: {media}')

if numeros != numeros:
    print (f'Maior numero: {max(numeros)}')
    print (f'Menor numero: {min(numeros)}')