'''
Lista 2 - Estrutura de Repetição - Média 10 valores
Faça um programa que calcule a média aritmética de 10 valores

Entrada: 10 números

Saida: A média aritimética entre os 10 números com duas casas decimais.

Exemplos de Entrada e Saída
Entrada:

1 2 3 4 5 6 7 8 9 10

Saída:

5.50

Entrada:

2 2 2 2 2 2 2 2 2 10

Saída:

2.80

'''

#le os dados e guarda em um vetor
vetor = [float(x) for x in input().split()]

#variavel acumlador
soma = 0.0

for valor in vetor:
    #soma cada velor no vetor
    soma+= valor

#divide a soma pelo tamanho do vetor
print('%.2f' %(soma/len(vetor)))