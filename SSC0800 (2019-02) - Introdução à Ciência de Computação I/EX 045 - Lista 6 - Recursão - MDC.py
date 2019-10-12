'''
Dados dois números inteiros X e Y

Calcule MDC(X,Y) recursivamente



'''

def mdc(x,y):

    if ( x == y ):
        return x;

    if ( x < y ):
        return mdc(y, x);

    return mdc(x-y,y);


x = int(input())
y = int(input())

print(mdc(x,y))