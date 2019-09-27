'''
Funções
'''
#função que valida se teve ganhador
def ganhador(m):


    #for para ver se teve ganhando na linha ou coluna
    for i in range(3):
        #verifica na linha
        if(  m[i][0]!='-' and m[i][0]==m[i][1] and m[i][0]==m[i][2]):

            print(m[i][0], "ganhou")
            return True

        #verifica na coluna
        elif (m[0][i]!='-' and m[0][i]==m[1][i] and m[0][i]==m[2][i]):

            print(m[i][0], "ganhou")
            return True
        
    #verifica nas diagonais
    if(m[1][1] != '-' and (((m[0][0]==m[1][1] and m[0][0])==m[2][2]) or (m[0][2]==m[1][1] and m[0][2]==m[2][0]))):

        print(m[1][1], "ganhou")
        return True

    else:
        return False

'''
Código Principal
'''
#matriz do jogo
m = []

#variavel que verifica se existe traço '-'
ExisteTraco = False

#realiza a leitura das linhas
for i in range(3):
    linha = input().replace("\r","").split(" ")
    
    #se não existe nenhum traçao ainda, verifica
    if(ExisteTraco==False):
        ExisteTraco = '-' in linha

    m.append(linha);

#verifica se houve ganhador
if(ganhador(m) == False):
    
    #verifica se existe valor - na matriz
    if ExisteTraco:
        print("em jogo")
    else:
        print("empate")
