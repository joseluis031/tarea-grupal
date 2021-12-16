import random

piedras_totales = random.randint(10,25)
print("Hay",piedras_totales,"piedras")
piedras_elegidas = 0

def vs(piedras_totales,piedras_elegidas):
    if piedras_totales == 2:
        piedras_elegidas = 2
    elif piedras_totales == 3:
        piedras_elegidas = 3
    elif piedras_totales == 5:
        piedras_elegidas = 5
    elif piedras_totales != 2 or 3 or 5:
        while True:
            piedras_elegidas = random.randint(2,5)
            if piedras_elegidas == 4:
                pass
    return piedras_elegidas


turnos = random.randint(1,2)
while piedras_totales > 1:
    if turnos == 2:
        print("Turno del jugador 1")
        piedras_elegidas = vs(piedras_totales, piedras_elegidas)
        if piedras_elegidas == 2:
            piedras_totales -= 2
            print("Ha retirado 2 piedras")
            print("Quedan:", piedras_totales, "piedras")
        elif piedras_elegidas == 3:
            piedras_totales -= 3
            print("Ha retirado 3 piedras")
            print("Quedan:", piedras_totales, "piedras")
        elif piedras_elegidas == 5:
            print("Ha retirado 5 piedras")
            print("Quedan:", piedras_totales, "piedras")
        break
    elif turnos == 2:
        print("Turno del jugador 2")
        if piedras_elegidas == 2:
            piedras_totales -= 2
            print("Ha retirado 2 piedras")
            print("Quedan:", piedras_totales, "piedras")
        elif piedras_elegidas == 3:
            piedras_totales -= 3
            print("Ha retirado 3 piedras")
            print("Quedan:", piedras_totales, "piedras")
        elif piedras_elegidas == 5:
            print("Ha retirado 5 piedras")
            print("Quedan:", piedras_totales, "piedras")
        break