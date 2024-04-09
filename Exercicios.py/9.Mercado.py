import os
os. system ("cls || clear")

descrição = input ("Produto: ")
quantidade = int (input("Quantidade: "))
preço = int(input ("Preço: "))


#APLICANDO AS CONDIÇÕES
if quantidade <= 5:
    desconto: int = 0.2 
elif quantidade > 5 and quantidade <= 10:
    desconto: int = 0.3
elif quantidade > 10:
    desconto: int = 0.5

#CALCULANDO
total: int = quantidade * preço
totalPago: int = total - desconto

#EXIBINDO OS RESULTADOS
print (f"NOME: {descrição}")
print (f"QUANTIDADE: {quantidade}")
print (f"TOTAL: {total}")
print (f"TOTAL PAGO: {totalPago}")