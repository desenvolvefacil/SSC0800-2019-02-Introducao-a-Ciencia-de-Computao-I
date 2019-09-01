'''
Lista 2 - Estrutura de Repetição - Tabuada
Faça um programa que mostre a tabuada (do 0 até o 10) de um determinado número.

Entrada: Um número inteiro

Saida: A tabuada do número.

Exemplos de Entrada e Saída
Entrada:

7
Saída:

0 7 14 21 28 35 42 49 56 63 70
'''

# le qual tabuada sera mostrada
num = int(input())

# realiza o calculo e mostra em tela
for i in range (11):
    #define o end como espaco em branco invés de \n
    print((num * i), end=' ')