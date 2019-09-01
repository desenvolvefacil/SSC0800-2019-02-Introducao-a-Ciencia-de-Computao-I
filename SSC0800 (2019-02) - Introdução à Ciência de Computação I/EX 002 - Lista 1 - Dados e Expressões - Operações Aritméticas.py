'''
Escreva um programa em pn2thon para realizar adição, subtração, multiplicação , divisão e modulo de dois números.

Input:
12, 5

Ouput:
A soma dos números dados é : 17
A subtração dos números dados é : 7 
O multiplicação dos números dados é : 60 
A divisão dos números dados é : 2.400000 
O modulo é = 2 
'''

#le os valores inteiros
n1, n2 = map(int,input().split(" "))

#Soma
print("x+y =",(n1 + n2))

#Subtração
print("x-y =" ,(n1 - n2))

#Multiplicação
print("x.y =" ,(n1 * n2))

#Divisão
print("x/y =", round(n1 / n2,6))

#Modulo
print("x mod y =",(n1 % n2))