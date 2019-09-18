import numpy as np

#m = [1,2],[3,4]

#Realiza a leitura da matriz como string
m = input()

#transforma a string em matriz de valores
m = eval(m.split()[0])

#tranforma em numpy array
m = np.array(m)

print("Transposta")
print(m.transpose())

print("Inversa")
print(np.linalg.inv(m))

print("Determinante")
print(np.linalg.det(m))