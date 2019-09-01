'''

Lista 3 - Funções - Soma Pares Parte I
Desenvolva um programa que leia quatro números inteiros e calcule a soma dos que forem par. Uma função chamada soma_par() deve receber esses quatro valores e retornar a soma dos pares.

Dica: use o seguinte print:

print("A soma dos numeros pares =", soma)
Exemplo de Entrada e Saída
Entrada:

2
0
4
3

Saída:

A soma dos numeros pares = 6

'''

'''
Função que recebe um vetor e soma seus valores
'''
def somaPar(vetor):
    soma = 0
    for valor in vetor:
        #soma o valor se for par ou 0 se for impar
        soma += (valor%2==0) and valor or 0

    return soma

#já que sabemos que o tamanho do vetor, inicamos ele com tamanho 4
vetor = [0,0,0,0]

#le os valores e guarda no vetor
for i in range(len(vetor)):
    vetor[i] = int(input())

print("A soma dos numeros pares =",somaPar(vetor))

