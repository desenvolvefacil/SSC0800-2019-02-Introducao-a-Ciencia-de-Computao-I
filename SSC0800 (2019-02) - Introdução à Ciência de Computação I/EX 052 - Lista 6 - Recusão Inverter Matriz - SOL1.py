import numpy as np

'''
https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.ndarray.shape.html

https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.reshape.html


[1,2],[3,4]

[1,2,3],[4,5,6]

[1,2,3],[4,5,6],[7,8,9]

[15,542,35],[454,521,621],[217,218,219],[98,2818,29819]

[1445,1542,8435,989],[454,4854,98521,54621],[458,21557,254218,221519],[54598,542818,9529819,98653]
'''

#Otimizado, pois não preciso saber o qdo trocar linha ou coluna

def inverter(m,esq,dir,numeroColunas):
    if (esq >= dir):
        return;

    #acha as posições a serem trocadas
    linhaEsq, colunaEsq = divmod(esq,numeroColunas)
    linhaDir, colunaDir = divmod(dir,numeroColunas)
    
    #realiza a troca dos valores
    m[linhaEsq][colunaEsq],m[linhaDir][colunaDir] = m[linhaDir][colunaDir],m[linhaEsq][colunaEsq]

    #chama recursivamente, andando 1 a esquerda e -1 a direita
    inverter(m,esq+1,dir-1, numeroColunas)


#inicio do programa

A = np.array(eval(input().split()[0]))

#pega a qtd de linhas e colunas para voltar a matriz ao tamanho original
linhas, colunas = A.shape

#pega o total de elementos dentro da matriz
totalElementos = linhas * colunas

#chama a função recursiva
inverter(A,0,totalElementos-1, colunas)

print(A)


