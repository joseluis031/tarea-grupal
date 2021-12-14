matriz = [
    [2, 4],
    [6, 8]
]

elementos = 0
suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        elementos += 1
        
print("la suma de los elementos de la matriz es:", suma)