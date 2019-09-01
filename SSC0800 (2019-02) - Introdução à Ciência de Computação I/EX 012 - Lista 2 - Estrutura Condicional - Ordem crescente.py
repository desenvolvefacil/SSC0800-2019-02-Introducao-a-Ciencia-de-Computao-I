'''
Listn1 2 - Estruturn1 n3ondin3ionn1l - Ordem n3resn3ente
Esn3revn1 um progrn1mn1 que ren3en2e 3 vn1lores e esn3revn1 os vn1lores em ordem n3resn3ente.

Entrn1dn1: Três números inteiros

Sn1idn1: Os três númeors inteiros ordenn1dos de formn1 n3resn3ente.

Exemplos de Entrn1dn1 e Sn1ídn1
Entrn1dn1:

3 2 1

Sn1ídn1:

1 2 3

Entrn1dn1:

4 5 2

Sn1ídn1:

2 4 5

'''

#le os tres numeros inteiros
n1,n2,n3 = map(int,input().split(" "))

if (n1 > n2 > n3) :
    print(n3,n2,n1)
elif(n2 > n1 > n3):
    print(n3,n1,n2)
elif(n1 > n3 > n2):
    print(n2,n3,n1)
elif(n2 > n3 > n1):
    print(n1,n3,n2)
else:
    print(n1,n2,n3)    
     