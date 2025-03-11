import os

#Limpar a tela
os.system("cls")

print('''
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█''')

#Entrada 
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operação = input("Digite a operação: ")

if(operação == "+"):
  resultado = numero1 + numero2
elif(operação == "-"):
  resultado = numero1 - numero2
elif(operação == "*"):
  resultado = numero1 * numero2
elif(operação == "/"):
  resultado = numero1 / numero2

#Saida
print("O Resultado foi: ", resultado)
print("A operação foi:", operação)


