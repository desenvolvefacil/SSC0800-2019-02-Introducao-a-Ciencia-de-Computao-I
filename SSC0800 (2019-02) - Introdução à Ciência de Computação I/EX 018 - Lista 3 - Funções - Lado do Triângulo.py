'''
Lista 3 - Funções - Lado do Triângulo
Desenvolva um programa onde o usuário fornece as medidas dos três lados de um triângulo e o tipo de triângulo (escaleno, isósceles ou equilátero) é escrito na tela. Lembre-se, você deve verificar também o critério de formação de triângulo, onde um lado qualquer não pode ser maior que a soma dos outros dois. Logo, o programa deve ter duas funções: uma função classificatriangulo() que recebe as medidas e imprime o tipo de triangulo, e uma função Ehtriangulo() que recebe as medidas e retorna 1 se for triangulo e 0, caso contrário.

Dica: Use os seguinte formatadores print:

print("Triangulo Equilatero")
print("Triangulo Isosceles")
print("Triangulo Escaleno")
print ("Valores nao formam um triangulo")

Exemplo de Entrada e Saída

Entrada:

2
3
4

Saída:

Triangulo Escaleno

'''

#Define se e ou não um triangulo
def ehTriangulo(ladoA,ladoB,ladoC):
    #retorna 1 se for triangulo 0 caso contrario
    if (ladoA+ladoC<ladoB or ladoC+ladoB<ladoA or ladoA+ladoB<ladoC):
       return 0
    return 1
       


def classificaTriangulo(ladoA,ladoB,ladoC):
    if(ladoA == ladoB == ladoC):
        return "Triangulo Equilatero"
    elif(ladoA==ladoB or ladoA==ladoC or ladoB==ladoC):
        return "Triangulo Isosceles"
    else:
        return "Triangulo Escaleno"

ladoA = int(input())
ladoB = int(input())
ladoC = int(input())

if(ehTriangulo(ladoA,ladoB,ladoC)==1):
    print(classificaTriangulo(ladoA,ladoB,ladoC))
else:
    print ("Valores nao formam um triangulo")