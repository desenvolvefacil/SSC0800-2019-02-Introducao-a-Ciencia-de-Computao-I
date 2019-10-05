import numpy as np


'''
Resolver um Sistema Linear Ax=b.

Dado um sistema linear de 3 equações, onde cada linha é uma equação resolva o sistema utilizando Numpy Linalg Solve

https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html


#Dica

Caso decida não montar as matrizes na mão, você poderá utilizar as seguintes funções para auxiliar no processo

https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromstring.html

https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html

#Dica 2

Caso decida montar a matriz na mão lembre-se que as entradas são de inteiros no padrão

Matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

Vetor = np.array([1,2,3])

Sistema Modelo

2a + 1b + 1c = 4
1a + 3b + 2c = 5
1a + 0b + 0c = 6

Entrada

2 + 1 + 1 = 4
1 + 3 + 2 = 5
1 + 0 + 0 = 6


1 + 1 + 2 = 9
1 + 2 + 1 = 8
2 + 1 + 1 = 7

Saida

[  6.  15. -23.]

'''


linha1, res1 = input().split("=")
linha2, res2 = input().split("=")
linha3, res3 = input().split("=")


linha1 = np.fromstring(linha1, dtype=int, sep='+')
linha2 = np.fromstring(linha2, dtype=int, sep='+')
linha3 = np.fromstring(linha3, dtype=int, sep='+')


A = np.array(linha1);
A = np.vstack([A,linha2])
A = np.vstack([A,linha3])

B = np.fromstring(res1+","+res2+","+res3, dtype=int,sep=",")

print(np.linalg.solve(A,B))
