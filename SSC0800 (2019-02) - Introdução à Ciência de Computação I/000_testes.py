class Carros(object):
    def __init__(self,ID,f,m,a,c,p):
        self.ID = ID
        self.fab = f
        self.modelo = m
        self.ano = a
        self.cor = c
        self.preco = p
        
    def getID(self):
        return self.ID
    
    def getFab(self):
        return self.fab
    
    def setFab(self, fab):
        self.fab = fab
        
    def __str__(self):
        return "Fab: "+self.fab+"\n" + "Mod: "+self.modelo+"\n" + "Cor: "+self.cor+"\n" + "Ano: "+self.ano+"\n" + "Pre: "+self.preco+"\n"

ls_carros = []

n = int(input())

for i in range(n):
     ID = input()
     f = input()
     m = input()
     c= input()
     a= input()
     p= input()
     ls_carros.append(Carros(ID,f,m,c,a,p))
     
op = int(input())

while(op != 0):
    if(op == 1):
        IDop = input()
        for carro in ls_carros:
            if(IDop == carro.getID()):
                print(carro)
    elif(op == 2):
        for carro in ls_carros:
            if(carro.getFab() == "Chevrolet"):
                carro.setFab("GM")
    elif(op == 3):
        for carro in ls_carros:
            print(carro)    
    op = int(input())