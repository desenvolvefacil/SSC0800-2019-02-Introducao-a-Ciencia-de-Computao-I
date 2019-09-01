'''
Lista 3 - Funções - Ângulos do Triângulo
Desenvolva um programa onde o usuário fornece as medidas dos três ângulos de um triângulo e o tipo de triângulo (agudo, obtuso ou retângulo) é escrito na tela. Lembre-se, você deve verificar também o critério de formação de triângulo, onde a soma dos ângulos internos de um triângulo deve ser 180 graus. Logo, o programa deve ter duas funções: uma função angulotriangulo() que recebe os ângulos e imprime o tipo de triângulo e uma função Ehtriangulo() que recebe os ângulos e retorna 1 se for triangulo e 0, caso contrário.

Dica: Use os seguintes formatadores de print:

print("Triangulo retangulo")
print("Triangulo obtuso")
print("Triangulo agudo")
print ("Valores nao formam um triangulo")

Exemplo de Entrada e Saída
Entrada:

90
45
45

Saída:

Triangulo retangulo
'''

'''
Funções
'''

#Define se é um triangulo
def ehTriangulo(anguloA,anguloB,anguloC):
	return anguloA + anguloB + anguloC == 180 and 1 or 0

#Define o tipo de triangulo
def anguloTriangulo(anguloA,anguloB,anguloC):
	
    tipoTriangulo = ""

    if(anguloA > 90 or anguloB > 90 or anguloC>90):
        tipoTriangulo="Triangulo obtuso"
    elif(anguloA ==90 or anguloB==90 or anguloC==90):
        tipoTriangulo = "Triangulo retangulo"
    else:
        tipoTriangulo = "Triangulo agudo"
    return tipoTriangulo


'''
Código Fonte
'''
anguloA = int(input())
anguloB = int(input())
anguloC = int(input())



if(ehTriangulo(anguloA,anguloB,anguloC) == 1):
	print(anguloTriangulo(anguloA,anguloB,anguloC))
else:
	print('Valores nao formam um triangulo')