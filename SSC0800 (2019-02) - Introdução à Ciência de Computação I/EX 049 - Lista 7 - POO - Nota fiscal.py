#Classe Produto
class Produto:
    codigo:int
    preco:float
    qtd:int = 0

    def setCodigo(self,codigo):
        self.codigo = int(codigo)

    def getCodigo(self):
        return self.codigo

    def setPreco(self,preco):
        self.preco = preco

    def getPreco(self):
        return self.preco

    def setQtd(self,qtd):
        self.qtd = qtd

    def getQtd(self):
        return self.qtd

    def getTotal(self):
        return self.preco * self.qtd

    def addQtd(self,qtd):
        self.qtd += qtd

    def __str__(self):
        return '#{}:    {}  {:.2f} {:.2f}\n'.format(self.codigo,self.qtd,self.preco,self.getTotal())
        #1:    1  2.19 2.19

    def str(self):
        return '#{}:    {}  {:.2f} {:.2f}\n'.format(self.codigo,self.qtd,self.preco,self.getTotal())

#classe nota fiscal
class NF:
    items = []


    def valorTotal(self):
        total = 0.0

        for p in self.items:
            total += p.getTotal()

        return total

    def addProduto(self,produto:Produto):
        
        self.items.append(produto)

        '''
        if any(produto.getPreco() in produto.codigo for p in self.items):
            p.setQtd(p.getQtd())
        else:
            self.items.append(produto)
        '''    

    def addQtd(self,cod,qtd):
        for p in self.items:
            if p.getCodigo() == cod:
                p.addQtd(qtd)
                break


    def __str__(self):
        
        #oredena a lista pelo codigo
        self.items = sorted(self.items, key = Produto.getCodigo)

        retorno = '#COD QTD VL_UN R$\n'

        for p in self.items:
            if p.getQtd()>0:
                retorno += p.str()


        retorno+='Total: R$ {:.2f}'.format(self.valorTotal())

        return retorno

#main

nf = NF()


#le os produtos
n = int(input())

for i in range(n):
    p = Produto()

    cod , valor = map(float,input().split(" "))

    p.setCodigo(cod)
    p.setPreco(valor)
    #p.setQtd(2)


    nf.addProduto(p)

#adiciona as qtd
n = int(input())

for i in range(n):
    cod, qtd = map(int,input().split(" "))

    nf.addQtd(cod,qtd)

print(nf)