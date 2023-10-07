#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#3)Escreva um programa utilizando o if (com elif e else se necessário), que receba
#dois números e um sinal, e faça a operação matemática definida pelo sinal.
#Soma, multiplicação, divisão, subtração, modal.

numero01=eval(input("DIGITE O 1° NUMERO: "))
numero02=eval(input("DIGITE O 2° NUMERO: "))


print("-------------------------")
print("' + ' - SOMA \n")
print("' - ' - SUBTRAÇÃO \n")
print("' * ' - MULTIPLICAÇÃO \n")
print("'/ ' - DIVISÃO")
opcao=input("INFORME A OPERAÇÃO DESEJADA: ")

if opcao=='+':
    soma=numero01+numero02
    print(soma)
elif opcao=='-':
    soma=numero01-numero02
    print(soma)
elif opcao=='*':
    soma=numero01*numero02
    print(soma)
else:
    soma=numero01/numero02
    print(soma)

