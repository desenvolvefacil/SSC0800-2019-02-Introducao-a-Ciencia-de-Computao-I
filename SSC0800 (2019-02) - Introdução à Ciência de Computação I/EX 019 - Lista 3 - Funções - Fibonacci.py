'''
Lista 3 - Funções - Fibonacci
Desenvolva uma função que receba um número n e retorne o n-ésimo termo da sequência de Fibonacci. O n-ésimo número da sequência de Fibonacci Fn é dado pela fórmula de recorrência abaixo. O programa principal fornece o número n para a função, recebe o resultado retornado pela função e imprime esse resultado.

Exemplos de Entrada e Saída
Entrada:

2

Saída:

1

Entrada:

6

Saída:

8
'''

#recebe um número N e retorna seu valor na sequência de fibonacci
def fibonacci(n):
    #para saber qual o promixo temos sempre que saber os dois ultimos valores
    n1 = 1
    n2 = 1

    #para 1 e 2 a o valor é 1 por definição, por isto começamos a partir do 3º número
    for i in range(3,n+1):
        #precisamos deslocar n1 e n2 para uma casa a frente, porém não podemos perder os valores; então utilizaremos uma variavel auxiliar
        aux = n2
        n2+=n1
        n1 = aux

    return n2

'''
Codigo Fonte
'''

n = int(input())

print(fibonacci(n))