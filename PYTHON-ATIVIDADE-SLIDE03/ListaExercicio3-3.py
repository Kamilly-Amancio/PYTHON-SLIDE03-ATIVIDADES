#NOME: KAMILLY AMANCIO BATISTA
#MATRICULA: 202202570397

#Faça um programa utilizando while e continue para contar de 1 a 10, porem
#nesse intervalo, verifique valores impares como no exemplo “numero % 2 ==
#1”. Se o número for ímpar, a instrução continue é acionada, o que faz com que
#o programa pule a impressão desse número e vá para a próxima iteração do
#loop. Isso resulta na impressão apenas dos números pares de 1 a 10.

numero=1

while numero<=10:
    if numero % 2 ==1:
        numero+=1
        continue

    print(numero)
    numero+=1


