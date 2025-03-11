import os

#Limpar a casa
os.system("cls")

print(''' 
█▀▄▀█ █▀▀ █▀█ █▀▀ ▄▀█ █▀▄ █▀█
█░▀░█ ██▄ █▀▄ █▄▄ █▀█ █▄▀ █▄█ ''')

nomeproduto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preço = float(input("Digite o preço unitario: "))

total = quantidade * preço 


if(quantidade <= 5):
    desconto = preço * 0.02
    print("O desconto sera de 2%: ")
elif(quantidade > 5 and quantidade <= 10):
    desconto = preço * 0.03
    print("O desconto sera de 3%: ")
elif(quantidade > 10):
    desconto = preço * 0.05
    print("O desconto sera de 5%: ")

print("Total a pagar sem desconto: " , total - desconto)
print("Total a pagar com desconto: " , total)


