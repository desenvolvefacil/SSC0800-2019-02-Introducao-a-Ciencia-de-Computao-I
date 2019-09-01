'''
Lista 2 - Estrutura de Repetição - Divisores
Desenvolva um algoritmo que leia um número N inteiro positivo e escreva os divisores desse valor.

Entrada: Um inteiro N, sendo N >= 0

Saida: Um linha para cada divisor do número N em ordem decrescente.

Exemplos de Entrada e Saída
Entrada:

10

Saída:

10
5
2
1

Entrada:

7

Saída:

7
1

'''

#le o numero
numero = int(input())

#roda até chegar em 0
for i in range(numero, 0, -1):
    #se for divisivel mostra em tela
    if (numero % i == 0):
        print(i)
