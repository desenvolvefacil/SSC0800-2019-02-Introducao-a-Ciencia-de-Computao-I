'''
Escreva um programa para calcular o volume de uma esfera, dado um raio r, e uma constante pi, considerando:
pi=3.14
volume = (4/3)pir^3 

input:

5

output:

(raio: 5 pi: 3.14 ) volume: 523.33

'''

raio = int(input())

#define o valor de pi
pi=3.14

#faz o calculo do volume
volume = (4/3)*pi*raio**3 

print("(raio:", raio, "pi:", pi,") volume:", round(volume,2))