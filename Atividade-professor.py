import os 

#Limpar tela
os.system("cls")

print(''' 
▒█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀█ 
▒█▄▄█ █▄▄▀ █░░█ █▀▀ █▀▀ ▀▀█ ▀▀█ █░░█ █▄▄▀ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ''')

nivel = int(input("Digite o nivel do professor: "))
quantidade = int(input("Digite a quantidade de aulas por semana: "))


if(nivel == 1):
    salario = (quantidade * 12.00) * 4

elif(nivel == 2):
    salario = (quantidade * 17.00) * 4

elif(nivel == 3):
     salario = (quantidade * 25.00) * 4


print("Resultado salario: " , salario)






