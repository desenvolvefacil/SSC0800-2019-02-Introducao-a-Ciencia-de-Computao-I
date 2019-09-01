'''
Lista 3 - Funções - Maior e Menor Real
Desenvolva um programa que receba 10 valores reais e utilize duas funções para retornar, respectivamente, o menor e o maior deles. O uso de funções é obrigatório. Em seguida, escreva o resultado com precisão de 2 casas decimais conforme exemplo.

Entrada: 10 números reais

Saida: Duas linhas, com o menor e o maior valor dentre os 10 valores digitados respectivamente. Utilize 2 casas decimais.

Exemplos de Entrada e Saída
Entrada:

1
10
14
4
95.4
8
15
43
17
3

Saída:

1.00
95.40

Entrada:

43.45
-1.22
-10.21
25.93
-25.85
48.14
80.22
18.98
10.63
46.92

Saída:

-25.85
80.22

'''

def menorValor(vetor):
    menor = vetor[0]
    
    for valor in vetor:
        menor = (menor > valor) and valor or menor

    return menor

def maiorValor(vetor):
    maior = vetor[0]
    
    for valor in vetor:
        maior = (maior < valor) and valor or maior

    return maior

vetor = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

for i in range(len(vetor)):
    vetor[i] = float(input())

menor = menorValor(vetor)
maior = maiorValor(vetor)

print('%.2f'%menor)
print('%.2f'%maior)