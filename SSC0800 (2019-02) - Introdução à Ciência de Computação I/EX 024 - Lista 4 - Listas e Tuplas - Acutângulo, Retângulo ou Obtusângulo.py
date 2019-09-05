'''
Dados 3 pontos no plano, decida se eles formam um triângulo ou não; em caso positivo, determinar se ele é acutângulo (todos seus ângulos internos medem menos que 90º), retângulo (possui um ângulo interno reto) ou obtusângulo (possui um ângulo interno de medida maior que 90º). Considere o exercício do produto escalar entre 2 vetores como dica, pense quando ele é positivo, zero ou negativo!

https://www.geeksforgeeks.org/find-all-angles-of-a-triangle-in-3d/

Entrada: 3 linhas, cada uma contendo um par de inteiros indicando as coordenadas (x,y) de cada ponto.

Saída: A string NAO, caso os pontos não formem um triângulo. Caso formem, imprima a string SIM, e na linha de baixo: A, caso seja acutângulo, R caso seja retângulo ou O caso seja obtusângulo.

Exemplos de Entrada e Saída

Entrada

0 4
0 0
3 0

saída

SIM
R

Entrada

5 4
3 2
6 1

saída

SIM
A

Entrada

0 0
-1 -1
1 1

saída

NAO

'''

#Acha o angulo atraves da inversa do cosseno**(-1)
def angulo(x1,y1,x2,y2,x3,y3):
    return (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)

def area(x1,y1,x2,y2,x3,y3):
    return 0.5 * (x1 * (y2 - y3) + y1 * (x3 - x2) + x2 * y3 - x3 * y2)

'''
Código Fonte
'''

#matrix que ira guardar os pontos
pontos = [0,1,2]


#le os dados x,y e guarda na matriz
for i in range(3):
    x , y = map(int,input().split(" "))
    pontos[i] = [x,y]

if area(pontos[0][0],pontos[0][1],pontos[1][0],pontos[1][1],pontos[2][0],pontos[2][1]):

    tipo = 'A'

    for i in range(3):
        #pegando os pontos da matriz só pra ficar mais fácil o entendimento
        #lembrando que os pontos variam conforme o angulo a ser analisado
        x1,y1 = pontos[(i) % 3]
        x2,y2 = pontos[(i + 1) % 3]
        x3,y3 = pontos[(i + 2) % 3]

        ang = angulo(x1,y1,x2,y2,x3,y3)

        #sao perpendiculares, ou seja, forma um angulo de 90º
        if(ang == 0):
            tipo = 'R'
            break
        #caso tenha um angulo maior que 90º
        elif(ang < 0):
            tipo = 'O'
            break

    print("SIM")
    print(tipo)

else:
    print('NAO')