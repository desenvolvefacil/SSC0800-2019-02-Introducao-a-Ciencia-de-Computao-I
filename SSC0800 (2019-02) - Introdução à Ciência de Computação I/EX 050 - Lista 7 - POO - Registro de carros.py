class Carros(object):
   
    def __init__(self,ID,fabricante,modelo,cor,ano,preco):
         self.ID = ID
         self.fabricante = fabricante
         self.modelo = modelo
         self.ano = ano
         self.cor = cor
         self.preco = preco
         
    def get_ID(self):
        return self.ID
    
    def get_fab(self):
        return self.fabricante
        
    def get_mod(self):
        return self.modelo
    
    def get_cor(self):
        return self.cor
    
    def get_ano(self):
        return self.cor
    
    def get_preco(self):
        return self.preco
    
    def set_fab(self,fabricante):
        self.fabricante = fabricante

    def __str__(self):
        return 'Fab: '+self.fabricante+'\n'+'Mod: '+self.modelo+'\n'+'Cor: '+self.cor+'\n'+'Ano: '+self.ano+'\n'+'Pre: '+self.preco+'\n'
                
         
lista = []
n = int(input())
for i in range(n):
    ID = input()
    fabricante = input()
    modelo = input()
    cor = input()
    ano = input()
    preco = input()
    lista.append(Carros(ID,fabricante,modelo,cor,ano,preco))

operacao = int(input())
while operacao != 0:
    if operacao == 1:
        #busca por ID
        ID = input()
        for carro in lista:
            if carro.get_ID() == ID:
                print(carro)
        
    elif operacao == 2:
        #Modifica fabricante pChevrolet para GM"
        for carro in lista:
            if carro.get_fab() == 'Chevrolet':
                carro.set_fab("GM")
    elif operacao == 3:
        "Imprimir os dados de todos os carros"
        for carro in lista:
            print(carro)
        
    operacao = int(input())
