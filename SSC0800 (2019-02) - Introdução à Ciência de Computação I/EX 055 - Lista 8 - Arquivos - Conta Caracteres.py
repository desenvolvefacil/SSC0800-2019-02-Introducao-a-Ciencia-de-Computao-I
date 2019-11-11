import string

#cria o dicionario com caracteres de a-z
dicDeLetras = dict.fromkeys(string.ascii_lowercase , 0)

#abre o arquivo
arquivo = open("texto.txt", 'r');

#le o texto
texto = arquivo.read().lower();

#fecha o arquivo
arquivo.close();

#le cada caractere do arquivo
for c in texto:
    #se for uma letra dentro do dicionario
    if c.isalpha():
        dicDeLetras[c] = dicDeLetras[c]+1


#mostra o resultado
for c in dicDeLetras:
    print(c ,'=',dicDeLetras[c])

