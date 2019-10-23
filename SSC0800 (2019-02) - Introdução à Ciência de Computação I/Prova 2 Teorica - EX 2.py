#aumenta o limite para recursão
import sys
sys.setrecursionlimit(2048)

def valorMenor(v, posicao ,n,menor):
    if posicao >= n:
        return menor;
    else:
        if(v[posicao]<menor):
            menor = v[posicao]

        return valorMenor(v,posicao+1,n,menor)

def valorMaior(v, posicao ,n,maior):
    if posicao >= n:
        return maior;
    else:
        if(v[posicao]>maior):
            maior = v[posicao]

        return valorMaior(v,posicao+1,n,maior)

def valorMedio(v,posicao,n,soma):
    if(posicao>=n):
        return soma // n
    else:
        soma = soma + v[posicao]

        return valorMedio(v,posicao + 1,n,soma)



n,opc = map(int,input().split(" "))

v = list(map(int,input().split(" ")))

if opc == 1:
    print(valorMenor(v,1,n,v[0]))
elif opc == 2:
    print(valorMaior(v,1,n,v[0]))
else:
    print(valorMedio(v,0,n,0))