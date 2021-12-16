import random

piedras_totales = random.randint(10,25)
print(piedras_totales)
piedras_elegidas = 0

def versus(piedras_totales,piedras_elegidas):
    if piedras_totales == 2:
        piedras_elegidas = 2
    elif piedras_totales == 3:
        piedras_elegidas = 3
    elif piedras_totales == 5:
        piedras_elegidas = 5
    else:
        while True:
            piedras_elegidas = random.randint(2,5)
            if piedras_elegidas == 4:
                pass
    return piedras_elegidas

versus(piedras_totales,piedras_elegidas)