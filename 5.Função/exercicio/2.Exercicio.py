import os

def logo ():
    os.system
    print ("="*10)
    print ("☄️☄️☄️   NASA ☄️☄️☄️")
    print ("="*10)

def operação (numero):
    for i in range (1,11):
        print (f"\t{numero} X {i} = {numero * i}")
    



logo ()
num = int (input ("Digite o seu numero: "))
operação (num)

