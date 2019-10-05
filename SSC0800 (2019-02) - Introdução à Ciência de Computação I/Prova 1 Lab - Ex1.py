import numpy as np

'''
#Resolver um Sistema Linear Ax=b.

Pelo cálculo da inversa de A, tq x=A^{-1}b
Usar a função NumPy Linalg Inv para facilitar o Calculo da Inversa A^{-1}

https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv

Temos então o modelo

2X + Y = 5
5X + 2Y = 3

Onde

Primeira Linha -> A = [2X,1Y],[5X,2Y]
Segunda Linha -> b = [5,3]

#Dica 1

Para realizar a solução utilize o operador @

Resultado = MatrizInversa @ b

#Dica 2

Utilize o conhecimento adquirido nas monitorias e laboratorios para realizar a leitura da matriz em uma só linha

Entrada

[2,1],[1,1]
[1,1]


[6,4],[5,2]
[1,2]

[6,4],[5,3]
[1,1]

[2,1],[5,2]
[5,3]

Saida

[-7. 19.]

'''

m1 = input()
m2 = input()

A = eval(m1.split()[0])
b = eval(m2.split()[0])

A = np.array(A)
b = np.array(b)

inv = np.linalg.inv(A)
print(inv @ b)