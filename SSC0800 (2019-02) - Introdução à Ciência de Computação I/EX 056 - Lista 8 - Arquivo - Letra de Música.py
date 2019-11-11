#abre o arquivo
arquivo = open("QuePaiseEste.txt", 'r');

#le o texto
texto = arquivo.read().lower().split();

#fecha o arquivo
arquivo.close();


p1,p2 = map(str, input().split())
n1,n2=0,0

for palavra in texto:
    if palavra == p1.lower():
        n1 += 1
    if palavra == p2.lower():
        n2 += 1

print(p1,n1,p2,n2)