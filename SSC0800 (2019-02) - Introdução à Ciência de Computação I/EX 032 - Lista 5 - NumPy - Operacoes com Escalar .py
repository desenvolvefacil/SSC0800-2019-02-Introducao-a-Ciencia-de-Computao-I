'''
Dado uma matriz M e um número escalar N realize: a multiplicação de (M * N) a soma de (M + N) a subtração (M - N) a divisão (M / N)

Exemplos de Entrada e Saída

Entrada:

[2,4,6],[10,20,30],[22,66,98]
2

Saída:

M * N
[[  4   8  12]
 [ 20  40  60]
 [ 44 132 196]]
M + N
[[  4   6   8]
 [ 12  22  32]
 [ 24  68 100]]
M - N
[[ 0  2  4]
 [ 8 18 28]
 [20 64 96]]
M / N
[[ 1.  2.  3.]
 [ 5. 10. 15.]
 [11. 33. 49.]]
'''

import numpy as np

#m = [2,4,6],[10,20,30],[22,66,98]'
#n = 2

#Realiza a leitura da matriz como string
m = input()

#transforma a string em matriz de valores
m = eval(m.split()[0])

#le o escalar N
n = int(input())

#tranforma em numpy array
m = np.array(m)

print("M * N")
print(m * n)
print("M + N")
print(m + n)
print("M - N")
print(m - n)
print("M / N")
print(m / n)
