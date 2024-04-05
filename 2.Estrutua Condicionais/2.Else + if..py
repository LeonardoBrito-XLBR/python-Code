import os
os.system("cls || clear")

nota : float 

nota = float (input ( "Digite a sua nota: "))

if nota >= 7:
    print ("Aprovado")
elif nota >= 5:
    print ("Recuperação")
elif nota >=4:
    print ("Conselho de classe")
else:
    print("Reprovado")

print ("==== FIM ====")