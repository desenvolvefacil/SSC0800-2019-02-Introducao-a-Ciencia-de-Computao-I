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


#Jeito roubado, mas aceitavel onde você tranforma a matriz em uma matriz linha (vulgo vetor) e depois volta a matriz na forma original

def inverte(v, esq, dir):

    if (esq >= dir):
        return;

    aux=0;
    aux = v[esq];
    v[esq] = v[dir];
    v[dir] = aux;
    inverte(v, esq+1, dir-1);


m1 = input()

A = eval(m1.split()[0])

A = np.array(A)

#pega a qtd de linhas e colunas para voltar a matriz ao tamanho original
linhas, colunas = A.shape

#converte em matriz linha, vulgo vetor para facilitar o processamento
A = np.reshape(A,(1,-1))

inverte(A[0],0,len(A[0])-1)

#redesenha a matriz com a configuração original
A = np.reshape(A,(linhas,colunas))

print (A)

