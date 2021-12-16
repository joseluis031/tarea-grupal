notas = [73,67,38,33]

multiplos_5_apartirde_40 = [40,45,50,55,60,65,70,75,80,85,90,95,100]


def notas_1estudiante():
    if notas[0] < 40:
        print("El estudiante 1 esta suspenso")
    elif notas[0] > 40:
        a = multiplos_5_apartirde_40[7] - notas[0]
        if a <= 3:
            print("La nota de estudiante 1 se redondeará a 75")
        
notas_1estudiante()

def notas_2estudiante():
    if notas[1] < 40:
        print("El estudiante 2 esta suspenso")
    elif notas[1] > 40:
        b = multiplos_5_apartirde_40[6] - notas[1]
        if b <= 3:
            print("La nota de estudiante 2 se redondeará a 75")
            
notas_2estudiante()

def notas_3estudiante():
    if notas[2] < 40:
        c = 40 - notas[2]
        if c <= 3:
            print("El estudiante 3 ha aprobado por redondeo")
        elif c >= 3:
            print("El estudiante 3 esta suspenso")
    elif notas[2] > 40:
        d = 40 - notas[2]
        if d <= 3:
            print("La nota de estudiante 3 se redondeará a 40")

notas_3estudiante()

def notas_4estudiante():
    if notas[3] < 40:
        e = 40 - notas[3]
        if e <= 3:
            print("El estudiante 3 ha aprobado por redondeo")
        elif e >= 3:
            print("El estudiante 4 esta suspenso")
    elif notas[3] > 40:
        f = 40 - notas[3]
        if f <= 3:
            print("La nota de estudiante 1 se redondeará a 40")
            
notas_4estudiante()