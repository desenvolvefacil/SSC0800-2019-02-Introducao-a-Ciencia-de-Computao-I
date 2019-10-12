'''
Implemente uma função recursiva que,
dados dois números inteiros x e n, calcula o
valor de x*n.
'''

def mult(x , n):
    if (n == 0):
        return n;
    else:
        return x + mult(x,n-1);



x = int(input());
n = int(input());

print(mult(x,n));