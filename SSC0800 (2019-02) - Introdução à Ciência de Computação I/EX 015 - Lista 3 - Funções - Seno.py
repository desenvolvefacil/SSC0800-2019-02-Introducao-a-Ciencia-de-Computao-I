'''
Lista 3 - Funções - Seno
Utilizando uma série de Taylor , o seno de um ângulo pode ser calculado aproximação encontrada na imagem em anexo, sendo x um ângulo em radianos (no primeiro quadrante do círculo trigonométrico).

Faça um programa que leia o ângulo x (número real) e a quantidade de iterações que se deve fazer para encontrar o seno. Seu programa deverá ter duas funções: uma para calcular o fatorial de um número e a outra para calcular o valor do seno de x. Na saída, o resultado deverá ter 6 casas decimais

[Seno: sen (X) = X - (X^3)/3! + (X^5)/5! - (X^7)/7! +....; (-1)^n.(X^(2n+1)/(2n+1)!)]

Exemplos de Entrada e Saída

Entrada:

0.785398 300

Saída:

0.707107

'''

# Funcao que calcula o seno:
def fseno(x, z):
    valor = 0.0                                                
    for i in range(z): 
        valor += ((((-1)**i) * (x**(2*i+1))) / fatorial(2*i+1))    
    return valor

# Funcao que calcula o fatorial:
def fatorial(x):
    valor = 1.0  #transformado em float para não esoturar o tipo int em grandes valores
    for i in range (1,x+1):
        valor *= i
    return valor


x, n = map(float, input().split(" "))
n = int(n)

# Calculando o valor do seno:
seno = fseno(x,n)
print('%.6f'%seno)