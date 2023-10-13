#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#Faça um programa utilizando o while com break, peça para o usuário digitar
#uma senha, se digitar a senha correta o programa para e informa que o acesso
#está concedido, se digitar a senha incorreta por até 3 vezes o programa informa
#que o acesso está negado e para.

senhaCorreta='1234'
tentativas=0

while True:

    senha=input("DIGITE A SENHA: ")

    if senha==senhaCorreta:
        print("Senha CORRETA!")
        break
    else:
        tentativas+=1
        print("SENHA INCORRETA")
    if tentativas>=3:
        print("ACESSO NEGADO!")
        break