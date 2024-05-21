import os
os.system ("cls || clear")


def Verificação (n1, n2):
   media = (n1 + n2) / 2
   return media

def Situacao (aluno):
    if aluno >= 7:
      Situacao = 'Aprovado'
    else:
      Situacao = 'Reprovado'
    return Situacao
   


num1 = float (input ("Digite o seu numero: "))
num2 = float (input ("Digite o seu numero: "))

total = Verificação (num1, num2)
letivo = Situacao (total) 


print (f"A sua média das suas notas: {total}")
print (f'A situação atual: {letivo}')
