'''
Lista 2 - Estrutura de Repetição - Resultado textual
Desenvolva um algoritmo que receba um numero inteiro n a ser elevado ao quadrado e escreva os dígitos do resultado por extenso.

Exemplos de Entrada e Saída
Entrada:

9

Saída:

Oito Um

Entrada:

200

Saída:

Quatro Zero Zero Zero Zero

'''

#define o vetor com os nomes dos numeros
numeros = ["Zero","Um", "Dois", "Três",  "Quatro", "Cinco",  "Seis",  "Sete", "Oito","Nove"]

#le o valor e eleva ao quadrado

valor = int(input()) ** 2

valor = str(valor)

for caractere in  valor:
    #pega cada caractere e imprime o nome em sua posicao no vetor numeros
    print(numeros[int(caractere)], end = " ")