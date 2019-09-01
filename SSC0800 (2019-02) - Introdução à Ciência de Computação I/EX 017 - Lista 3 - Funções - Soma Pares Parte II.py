'''
Lista 3 - Funções - Soma Pares Parte II
Faça um programa que leia uma sequência de números terminada em -1 e imprima a soma dos números pares lidos. Dica: Utilize a função implementada no exercício Soma Pares Parte I.

Entrada: Sequência de números com tamanho desconhecido terminada em -1

Saida: A soma dos números pares lidos

Exemplos de Entrada e Saída
Entrada:

7 5 2 2 6 9 8 7 -1

Saída:

18

Entrada:

-1

Saída:

0
'''

def somaPar(vetor):
    soma = 0
    for valor in vetor:
        #roda enquanto não for -1
        if(valor !=-1):
            #soma o valor se for par ou 0 se for impar
            soma += (valor%2==0) and valor or 0
        else:
            break

    return soma


'''
Código Fonte
'''

#Le os valores e guarda em um vetor
vetor = list(map(int,input().split(" ")))


print(somaPar(vetor))