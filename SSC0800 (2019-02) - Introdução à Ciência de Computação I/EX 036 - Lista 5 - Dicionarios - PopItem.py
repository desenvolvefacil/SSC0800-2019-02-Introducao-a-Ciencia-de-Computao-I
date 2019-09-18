'''
4
Yan 1234-5678
Pedro 9999-9999
Ana 8765-4321
Marina 8877-7788
'''

n = int(input())

dic = {}

for i in range(n):
    nome,tel = input().replace("\r","").split(" ")
    dic[nome]=tel


#dic = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),('Ana', '8765-4321'), ('Marina', '8877-7788')]

#print( 'yan' in  dic)

while(len(dic)>0):
    print(dic.popitem())