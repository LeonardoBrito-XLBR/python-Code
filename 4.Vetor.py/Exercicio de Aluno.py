import os 
os. system ("cls || clear")

notas = []
c: int = 0


for i in range (4):
    nota: float = (input (f"Sua {i +1} nota {notas[i]}:  "))
    notas.append(nota)
    c+=1
    media = sum(notas) / c
print ()


if media >= 7:
    resultado = 'Aprovado'
elif media >= 5:
    resultado = 'Recuperação'

else:
    resultado = 'Reprovado'


for i in (len (notas)):
    print (f'A SUAS NOTAS {notas [i]}')

print (media)
print (resultado)