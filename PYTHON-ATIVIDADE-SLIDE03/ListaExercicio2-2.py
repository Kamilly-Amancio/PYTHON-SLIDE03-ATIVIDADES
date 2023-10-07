#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#Faça um programa utilizando o for com string, que receba
#uma palavra digitada pelo usuário e verifique quantas
#vogais possui.

palavra=input("--DIGITE A PALAVRA: ")

quantVogais=0

for letra in palavra:
    if letra.lower() in 'aeiou':
        quantVogais+=1

print("QUANTIDADE DE VOGAIS NA PALAVRA:", palavra,"É: ", quantVogais)