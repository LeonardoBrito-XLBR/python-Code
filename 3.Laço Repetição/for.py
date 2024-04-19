import os
os.system ("cls || clear")


numero = int (input ("Digite o seu numero: "))

for c in range (1,11):
   print (f"{numero} x {c} = {numero * c} ")

opcao = input ("Quer um novo numero? ")

if opcao == 's':
   n2:  int = (input ("Digite o seu numero: "))

   for i in range (10):
    print(f"{n2} x {i * 2} = { n2 * i}")
else:
   print ("Adeus até mais")