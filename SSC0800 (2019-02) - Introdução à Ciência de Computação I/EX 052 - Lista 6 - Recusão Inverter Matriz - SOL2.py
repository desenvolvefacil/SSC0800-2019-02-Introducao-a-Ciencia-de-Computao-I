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

#jeito intuitivo, geralmente o pessoal sai por esta solução
def inverter(m, esqLinha, esqColuna, dirLinha, dirColuna, numeroColunas):
    
    #aqui vou fazer uma conta pra saber qdo parar
    if ((esqLinha *100 + esqColuna) >= (dirLinha * 100 + dirColuna )):
        return;
    
    #realiza a troca dos valores
    m[esqLinha][esqColuna], m[dirLinha][dirColuna] = m[dirLinha][dirColuna], m[esqLinha][esqColuna]


    #anda uma coluna a frente
    esqColuna += 1

    #caso estoure a coluna, posiciona pra linha de baixo
    if(esqColuna >= numeroColunas):
        esqColuna = 0
        esqLinha += 1

    #anda uma coluna pra trás
    dirColuna -= 1

    #caso estoure a coluna, posiciona pra linha acima
    if(dirColuna < 0):
        dirColuna = numeroColunas -1
        dirLinha -= 1

    #chama recursivamente
    inverter(m, esqLinha, esqColuna, dirLinha, dirColuna, numeroColunas)


#inicio do programa

A = np.array(eval(input().split()[0]))

#pega a qtd de linhas e colunas para voltar a matriz ao tamanho original
linhas, colunas = A.shape

#pega o total de elementos dentro da matriz
totalElementos = linhas * colunas

#chama a função recursiva
inverter(A, 0, 0, linhas-1, colunas-1, colunas)

print(A)

