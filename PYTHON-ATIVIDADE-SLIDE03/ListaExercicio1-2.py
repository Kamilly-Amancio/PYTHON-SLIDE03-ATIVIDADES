#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#2)Faça um programa utilizando o if (com elif e else se necessário), que receba
#quatro notas do tipo inteiro e o nome do tipo string de dois alunos, digitadas
#pelo usuário e calcule a média. No final informe o nome e se a nota for maior
#ou igual a sete, escreva aprovado, se for menor que 4, reprovado, senão
#escreva recuperação.

nomeAluno1=input("DIGITE O NOME DO PRIMEIRO ALUNO: ")
nota1Aulno1=eval(input("DIGITE A NOTA 01:"))
nota2Aulno1=eval(input("DIGITE A NOTA 02:"))
nota3Aulno1=eval(input("DIGITE A NOTA 03:"))
nota4Aulno1=eval(input("DIGITE A NOTA 04:"))

media1=((nota1Aulno1+nota2Aulno1+nota3Aulno1+nota4Aulno1)/4)


nomeAluno2=input("DIGITE O NOME DO SEGUNDO ALUNO: ")
nota1Aulno2=eval(input("DIGITE A NOTA 01:"))
nota2Aulno2=eval(input("DIGITE A NOTA 02:"))
nota3Aulno2=eval(input("DIGITE A NOTA 03:"))
nota4Aulno2=eval(input("DIGITE A NOTA 04:"))

media2=((nota1Aulno2+nota2Aulno2+nota3Aulno2+nota4Aulno2)/4)

if media1 and media2>=7:
    print(nomeAluno1)
    print(media1)
    print(nomeAluno2)
    print(media2)
    print("APROVADO!")
else:
    print(nomeAluno1)
    print(media1)
    print(nomeAluno2)
    print(media2)
    print("REPROVADO!")

