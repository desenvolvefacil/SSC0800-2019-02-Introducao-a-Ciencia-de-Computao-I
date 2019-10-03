
#função media
def media(v,n):
    soma = 0

    for i in v:
        soma+=i

    return soma/n

#função maior
def maior(v,n):
    m = v[0]

    for i in v:
        if i>m:
            m = i

    return m

def variancia(v,n):
    var = 0.0

    for i in v:
        var += (i - media(v,n))**2

    return var/n


'''
Inicio do Codigo
'''

#le o tamanho
n = int(input())

#le o vetor de inteiros
v = list(map(int,input().split(" ")))


print("Maior: %.2f" % maior(v,n))
print("Media: %.2f" % media(v,n))
print("Variancia: %.2f" % variancia(v,n))


