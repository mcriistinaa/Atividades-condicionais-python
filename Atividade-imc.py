import os

#limpar tela
os.system("cls")

print(''' 
██╗███╗░░░███╗░█████╗░
██║████╗░████║██╔══██╗
██║██╔████╔██║██║░░╚═╝
██║██║╚██╔╝██║██║░░██╗
██║██║░╚═╝░██║╚█████╔╝
╚═╝╚═╝░░░░░╚═╝░╚════╝░ ''')

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura * altura)

if(imc <= 16.9):
   print("Muito abaixo do peso: ")

elif(imc >= 17 and imc <= 18.4):
   print("Abaixo do peso: ")

elif(imc >= 18.5 and imc <= 24.9):
   print("Peso normal: ")

elif(imc >= 25 and imc <= 29.9):
   print("Acima do peso: ")

elif(imc >= 30 and imc <= 34.9):
   print("Obesidade grau I")

elif(imc >= 35 and imc <= 40):
   print("Obesidade grau II")

elif(imc >= 40):
   print("Obesidade grau III")

print("Sei imc sera: " , imc)