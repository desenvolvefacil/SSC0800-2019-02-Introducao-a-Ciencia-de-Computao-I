'''
Dados dois números inteiros X e Y

Calcule MDC(X,Y) recursivamente



'''

def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1) + fib(n-2))


x = int(input())

print(fib(x))