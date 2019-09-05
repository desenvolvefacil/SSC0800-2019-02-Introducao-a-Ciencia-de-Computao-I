'''
Dado um polígono simples (ou seja, um polígono cujos lados não adjacentes não se interceptam) P0P1P2...Pn-1 de n vértices, determinar se ele é côncavo ou convexo. Entrada: Um inteiro n>=3, indicando o número de vértices do polígono Em seguida, n linhas, contendo cada uma um par (x,y) de inteiros, representando o ponto P0,P1,P2,...,Pn-1 Obs: as arestas formadas são P0P1,P1P2,...,Pn-2Pn-1,Pn-1P0.

Saída: A string CONVEXO caso o polígono seja convexo, ou a string NAO CONVEXO, caso contrário.

Dica: se os pontos Pi=(x[i],y[i]), Pj=(x[j],y[j]), Pk=(x[k],y[k]) estão dispostos, nessa ordem, no sentido anti-horário, então o determinante da matriz ilustrada na imagem em arquivo abaixo será positivo. Se estiverem dispostos no sentido horário, será negativo. Tente desenhar alguns casos para ter uma ideia!

Exemplos de Entrada e Saída
Entrada:

5
0 0
1 0
2 3
-1 4
-3 1

Saída:

CONVEXO

Entrada:

7
1 2
5 3
4 5
3 4
2 6
0 3
2 3

Saída:

NAO CONVEXO
'''

#le o total de pontos que entram
tamanho = int(input())

pontos = []

for i in range(tamanho):
    x,y = map(int,input().split(" "))
    pontos.append([x,y])

def determinante(x1,y1,x2,y2,x3,y3):
    return (x1 * (y2 - y3) + y1 * (x3 - x2) + x2 * y3 - x3 * y2)

#calcula a primeira tripla de pontos para comparar com os demais
x1,y1 = pontos[0]
x2,y2 = pontos[1]
x3,y3 = pontos[2]
primeiratripla = determinante(x1,y1,x2,y2,x3,y3)

ehconvexo = True
#avalia sempre de 3 em 3 pontos
for i in range(tamanho):
    x1,y1 = pontos[(i) % tamanho]
    x2,y2 = pontos[(i + 1) % tamanho]
    x3,y3 = pontos[(i + 2) % tamanho]

    #calcula o determinante e compara com a primeira tripla de pontos
    #caso = 0 formam uma reta
    #caso < 0 não pode ser convexo
    if(determinante(x1,y1,x2,y2,x3,y3)) * primeiratripla < 0:
        ehconvexo = False
        break

#imprime com if ternario
print(ehconvexo == True and "CONVEXO" or "NAO CONVEXO")