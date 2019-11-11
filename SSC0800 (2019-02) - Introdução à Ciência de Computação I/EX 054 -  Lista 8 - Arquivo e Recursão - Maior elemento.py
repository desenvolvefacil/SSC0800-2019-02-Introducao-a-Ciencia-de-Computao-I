def indiceMaior(lista, posAtual,posMaior,n):
    if(posAtual>=n):
        return posMaior;
    else:
        posMaior = lista[posAtual]>lista[posMaior] and posAtual or posMaior

        return indiceMaior(lista, posAtual+1 ,posMaior,n)




#inicio do codigo

#abre o arquivo
arquivo = open("dados.txt", 'r');

#le a primeira linha
n = int(arquivo.readline());

#le a segunda linha
lista = list(map(float,arquivo.readline().split()));

#fecha o arquivo
arquivo.close();

posMaior = indiceMaior(lista,1,0,n);

print("Valor Maior: %.2f" % lista[posMaior]);
print("Pos Maior:", posMaior);

