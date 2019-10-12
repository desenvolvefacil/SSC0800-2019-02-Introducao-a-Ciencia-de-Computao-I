'''
Implemente uma função recursiva que,
dados dois números inteiros x e n, calcula o
valor de x^n.
'''

def pot(x , n):
   if ( n == 0 ):
       return 1;
   return ( x * pot(x, n-1));


x = int(input());
n = int(input());

print(pot(x,n));