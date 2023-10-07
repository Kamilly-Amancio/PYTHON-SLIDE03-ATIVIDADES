#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#Faça um programa utilizando o for com list, que realize a
#soma de todos os valores contidos em uma lista de
#números. Exemplo: numeros = [10, 20, 30, 40, 50]

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print(somalista([10,20,30,40,50]))
