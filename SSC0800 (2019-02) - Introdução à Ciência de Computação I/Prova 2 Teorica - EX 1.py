def contarCaracteres(senha, posicao, n, v):
    if(posicao>=n):
        return
    else:
        if senha[posicao] >= 'a' and senha[posicao] <= 'z':
            v[0] += 1
        elif senha[posicao] >= '0' and senha[posicao] <= '9':
            v[1] += 1
        else:
            v[2] += 1

        contarCaracteres(senha, posicao+1, n,v)

'''
[0] = alfabeto
[1] = numeros
[2] = resto

usei vetor, pois todo vetor é passagem por referencia
'''
v = [0,0,0]

senha = input().rstrip().lower()

contarCaracteres(senha, 0, len(senha) , v)

print(v[0],v[1],v[2])



