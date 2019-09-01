'''
Lista 2 - Estrutura de Repetição - Menores
Faça um programa que dado um número X e 10 números inteiros, imprima quantos números são menores que X.

Entrada: Um número inteiro X seguido de 10 números inteiros

Saida: A quantidade de números menores que X

Exemplos de Entrada e Saída
Entrada:

4
25 68 4 7 200 55 66 18 29 3

Saída:

1
'''

#numero que vai ser comparado
numero = int(input())

#vetor com os 10 valores
vetor = list(map(int,input().split(" ")))

#quantidade de valores no vetor menores que o numero
contador = 0

for valor in vetor:
    if(valor < numero):
        contador += 1

print(contador)
