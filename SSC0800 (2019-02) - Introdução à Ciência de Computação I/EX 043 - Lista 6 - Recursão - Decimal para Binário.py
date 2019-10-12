'''
Um problema típico em ciência da computação consiste
em converter um número da sua forma decimal para a
forma binária.

Dado um inteiro X printe para seu respectivo binário em tela

'''

def bin(x):
    if ( x == 0 ):
        return;

    bin(x // 2);
    print(x % 2, end="");
    



x = int(input())

bin(x)