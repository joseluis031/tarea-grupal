import random

piedras_totales = random.randint(10,25)
print("Hay",piedras_totales,"piedras")
piedras_elegidas = 0

def vs(piedras_totales,piedras_elegidas):
    if piedras_totales == 2:
        p = 2
    elif piedras_totales == 3:
        p = 3
    elif piedras_totales == 4:
        p = 3
    elif piedras_totales == 5:
        p = 5
    elif piedras_totales == 6:
        p = 5
    elif piedras_totales >=7:
        while True:
            p = random.randint(2,5)
            if p == 4:
                pass
            else:
                break
    return p


turnos = 1
while piedras_totales > 1:
    if turnos == 1:
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
            piedras_totales -= 5
            print("Ha retirado 5 piedras")
            print("Quedan:", piedras_totales, "piedras")
        turnos = 2
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
            piedras_totales -=5
            print("Ha retirado 5 piedras")
            print("Quedan:", piedras_totales, "piedras")
        turnos = 1
while piedras_totales < 2:
    if turnos == 2:
        print("No puedes quitar mas piedras, ha ganado el jugador 1")
        break
    elif turnos == 1:
        print("No puedes quitar mas piedras, ha ganado el jugador 2")
        break
    