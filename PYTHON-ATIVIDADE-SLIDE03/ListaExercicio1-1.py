#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#1)Faça um programa utilizando o if (com elif e else se necessário), que receba a
#idade do usuário e diga se ele é uma criança (0 a 11), adolescente (12 a 17),
#adulto (18 a 59) ou idoso

idade=eval(input("DIGITE A SUA IDADE:"))

if idade >=0 and idade <=11:
    print("! VOCÊ É UMA CRIANÇA !")
elif idade >=12 and idade <=17:
    print("! VOCÊ É UM ADOLESCENTE !")
else:
    print("! VOCÊ É UM ADULTO !")