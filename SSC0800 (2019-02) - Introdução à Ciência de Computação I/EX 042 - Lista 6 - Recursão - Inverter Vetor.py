'''
Dado um VETOR de inteiros, inverta a posição dos seus elementos.0 1 2 3 4 5 6 7 8 9[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]8 -10 65 -89 123 86 13215 89564
'''

def inverte(v, esq, dir):

    if (esq >= dir):
        return;

    aux=0;
    aux = v[esq];
    v[esq] = v[dir];
    v[dir] = aux;
    inverte(v, esq+1, dir-1);


vetor = list(map(int,input().split(" ")))

inverte(vetor,0,len(vetor)-1)

print(vetor)
