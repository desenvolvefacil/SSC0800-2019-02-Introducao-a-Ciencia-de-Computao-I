#classe Pokemon
class Pokemon():
    #identificado
    __id:int
    #nome
    __nome:str
    #poder de ataque
    __attack:int
    #poder de defesa
    __defense:int
    #vida/energia
    __stamina:int

    def __init__(self, id, nome, attack, defense, stamina):
        self.__id = id
        self.__nome = nome
        self.__attack = attack
        self.__defense = defense
        self.__stamina = stamina

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_stamina(self):
        return self.__stamina

    def __str__(self):
        return "{:10.10} {}  {}  {}".format(self.__nome,self.__attack,self.__defense,self.__stamina)


'''Quick Sort
atributo 1 attack | 2 defense | 3 stamina
'''

def particionar(lista, inicio, fim, atributo):
    pivo = lista[fim]
    inferior = inicio-1
    superior = fim

    valor_pivo = 0
    valor_inferior = 0
    valor_superior = 0

    

    ok = 0
    while not ok:

        while not ok:
            inferior = inferior + 1

            if(atributo == 1):
                valor_inferior = lista[inferior].get_attack()
                valor_superior = lista[superior].get_attack()
                valor_pivo = lista[fim].get_attack()
            elif(atributo == 2):
                valor_inferior = lista[inferior].get_defense()
                valor_superior = lista[superior].get_defense()
                valor_pivo = lista[fim].get_defense()
            else:
                valor_inferior = lista[inferior].get_stamina()
                valor_superior = lista[superior].get_stamina()
                valor_pivo = lista[fim].get_stamina()



            if inferior == superior:
                ok = 1
                break

            if valor_inferior > valor_pivo:
                lista[superior] = lista[inferior]
                break

        while not ok:
            superior = superior-1

            if(atributo == 1):
                valor_inferior = lista[inferior].get_attack()
                valor_superior = lista[superior].get_attack()
                valor_pivo = lista[fim].get_attack()
            elif(atributo == 2):
                valor_inferior = lista[inferior].get_defense()
                valor_superior = lista[superior].get_defense()
                valor_pivo = lista[fim].get_defense()
            else:
                valor_inferior = lista[inferior].get_stamina()
                valor_superior = lista[superior].get_stamina()
                valor_pivo = lista[fim].get_stamina()

            if superior == inferior:
                ok = 1
                break

            if valor_superior < valor_pivo:
                lista[inferior] = lista[superior]
                break

    lista[superior] = pivo
    return superior

def quicksort(lista, inicio, fim, atributo):
    if inicio < fim:
        split = particionar(lista, inicio, fim, atributo)
        quicksort(lista, inicio, split-1, atributo)
        quicksort(lista, split+1, fim, atributo)
    else:
        return



'''Fim Quick Sort
'''

        
buba = Pokemon(1,"buba", 1, 3, 2)
charm = Pokemon(2,"charm", 2, 5, 1)
pika = Pokemon(3,"pika", 3, 1, 3)

lista1 = []
lista1.append(buba)
lista1.append(charm)
lista1.append(pika)

lista2 = []
lista2.append(buba)
lista2.append(charm)
lista2.append(pika)

lista3 = []
lista3.append(buba)
lista3.append(charm)
lista3.append(pika)



print("ordena pelo poder de ataque")

quicksort(lista1,0,len(lista1)-1,1)

for pk in lista1:
    print(pk)

print()

print("ordena pela defesa")

quicksort(lista2,0,len(lista2)-1,2)

for pk in lista2:
    print(pk)


print()

print("ordena pela stamina")

quicksort(lista3,0,len(lista3)-1,3)

for pk in lista3:
    print(pk)
