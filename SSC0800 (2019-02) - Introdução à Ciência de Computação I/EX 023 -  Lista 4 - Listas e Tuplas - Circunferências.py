'''
Dados N (N>=3) pontos no plano, determinar se existe algum subconjunto de 3 elementos que determina uma circunferência de raio R. Dica: pense na equação de uma circunferência!

Entrada: Na primeira linha, dois inteiros: N e R, indicando o número de pontos e o raio da circunferência; em seguida, N linhas, cada uma contendo um par (x,y) de inteiros indicando os pontos no plano xy. Saída: O caractere S, caso exista um trio de pontos que determina uma circunferência, ou o caractere N, caso contrário.

Exemplos de Entrada e Saída
Entrada

4 2
2 0
0 2
1 1
0 -2

Saída

S

(Nesse caso, os pontos (2,0), (0,2) e (0,-2) determinam uma circunferência de raio 2)

Entrada

4 7
1 1
-1 2
0 0
0 -3
Saída

N

'''

#calcula a area de uma circunferencia dado 3 pontos
'''
1/2 * determinante da matriz

1 * |x2−x1 y2−y1|
2   |x3−x1 y3−y1|
'''
def area(x1,y1,x2,y2,x3,y3):
    return 0.5 * abs(y1 * (x2 - x3) + y2 * (x3 - x1) + y3 * (x1 - x2))

#n é número de pontos (x,y) que vão entrar, r é o tamanho do raio e ser
#comparado
n , r = map(int,input().split(" "))

pontos = []
#começa a ler do primeiro ponto
for i in range(n):
    # le os pontos
    x,y = map(int,input().split(" "))
    #adiciona os pontos na matriz
    pontos.append([x,y])

resultado = "N"

#comeca do primeiro ponto até o anti penultimo
for i in range(n - 2):
    #comeca do segundo ponto até o penultimo
    for j in range(i + 1,n - 1):
        #começa do terceiro ponto até o final
        for k in range(j + 1,n):
            #recupera o valor dos pontos, apenas para ficar mais fácil o
            #entendimento
            x1,y1 = pontos[i]
            x2,y2 = pontos[j]
            x3,y3 = pontos[k]

            #verifica se os 3 pontos forma uma área
            if(area(x1,y1,x2,y2,x3,y3) > 0):
                #pega o ponto X do centro
                xc = ((y1 - y3) * ((x1 ** 2) + (y1 ** 2) - (x2 ** 2) - (y2 ** 2)) + (y2 - y1) * ((x1 ** 2) + (y1 ** 2) - (x3 ** 2) - (y3 ** 2))) / (2 * (y1 - y3) * (x1 - x2) + 2 * (y2 - y1) * (x1 - x3))

                #pega o ponto Y do centro
                yc = 0.0

                if y1 != y2:
                    yc = (x1 ** 2 - x2 ** 2 - 2 * xc * (x1 - x2) + y1 ** 2 - y2 ** 2) / (2 * (y1 - y2))
                else:
                    yc = (x1 ** 2 - x3 ** 2 - 2 * xc * (x1 - x3) + y1 ** 2 - y3 ** 2) / (2 * (y1 - y3))

                #faz o calculo do raio já que encontramos os pontos centrais
                raio = (x1-xc)**2+(y1-yc)**2
                
                if raio == r**2:
                    resultado = "S"
                    break;break;break;

print(resultado)