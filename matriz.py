import random

matriz = [
    [random.randint(0,10),random.randint(0,10)],
    [random.randint(0,10),random.randint(0,10)]
]
print(matriz)
elementos = 0
suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        elementos += 1
        
print("la suma de los elementos de la matriz es:", suma)        