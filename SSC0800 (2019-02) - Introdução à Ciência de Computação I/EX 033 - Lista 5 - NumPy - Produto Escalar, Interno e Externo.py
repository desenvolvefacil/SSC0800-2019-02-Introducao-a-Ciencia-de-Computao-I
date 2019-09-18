import numpy as np

#m = [1,1,1]
#m2 = [1,1,1]

#Realiza a leitura da matriz como string
m1 = input()
m2 = input()

#transforma a string em matriz de valores
m1 = eval(m1.split()[0])
m2 = eval(m2.split()[0])

#tranforma em numpy array
m1 = np.array(m1)
m2 = np.array(m2)

print("Produto Escalar")
print(np.vdot(m1, m2))

print("Produto Interno")
print(np.inner(m1, m2))

print("Produto Externo")
print(np.outer(m1, m2))