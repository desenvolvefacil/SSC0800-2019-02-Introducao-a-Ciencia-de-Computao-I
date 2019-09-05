'''
Uma sequência pode ser interpretada como uma lista finita de termos. Faça um programa que leia um numero N; em seguida, na linha debaixo, leia todos os elementos de uma sequência de inteiros, armazene-os numa lista e verifique se existe uma subsequência tal que a soma dos termos é N, imprimindo "SIM" em caso positivo e "NAO" em caso negativo. Obs: uma subsequência é formada pegando uma parte da sequência original, sem pular nenhum termo; por exemplo, se (2,3,4,11,6,7,8) é a nossa sequência, (4,11,6) e (2) são subsequências dela, enquanto que (3,11,6,7) não é.

Entrada: Um inteiro N

Saída: A string SIM, caso haja uma subsequência cuja soma dos termos seja N; caso contrário, imprima a string NAO.

Exemplos de Entrada e Saída
Entrada:

12
1 2 3 4 5

Saída:

SIM

(A subsequência (3,4,5) tem soma dos termos igual a 12)

Entrada:

12
8 3 4

Saída:

NAO

'''

#le o valor
valor = int(input())

vetor = list(map(int,input().split(" ")))

resultado = "NAO"

#compara o primeiro valor com os proximos
for i in range(len(vetor)):
    soma = vetor[i]

    #soma os proximos e verifica se deu a soma
    for j in range(i + 1,len(vetor)):
        soma +=vetor[j]

        #caso encontre para os 2 for
        if soma == valor:
            resultado = "SIM"
            break
            break

print(resultado)