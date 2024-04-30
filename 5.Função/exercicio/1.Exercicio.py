import os

def tabuada ():
    os.system ("cls || clear")
    print ("==== NASA ====")

def operação (n1,n2):
    soma = (n1 + n2) 
    media = soma / 2
    return f"A soma: {soma}", f"A media final: {media}"

tabuada ()
num1 = int (input ("Numero 1: "))
num2 = int (input ("Numero 2: "))

tabuada ()
resultado = operação (num1, num2)

print (resultado)
