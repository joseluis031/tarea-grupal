import random

matriz = [
    [random.randint(1000,1000000), random.randint(1000,1000000),random.randint(1000,1000000)],
    [random.randint(1000,1000000), random.randint(1000,1000000), random.randint(1000,1000000)]
]
def print_matriz(matriz):
    for i in range(2):
        print(matriz[i])
        
print_matriz(matriz)
        
elementos = 0
suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        elementos += 1
        
print("la suma de los elementos de la matriz es:", suma)