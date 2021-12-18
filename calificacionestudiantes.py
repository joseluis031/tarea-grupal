notas = [73,67,38,33]

for i in range(len(notas)):
    if notas[i] > 40:
        print("El alumno {} ha aprobado".format(i+1))
    else:
        print("EL alumno {} ha suspendido".format(i+1))

for i in range(len(notas)):
    cociente = int(notas[1]/5 + 1)
    multiplo = cociente * 5
    if (multiplo-notas[i]) <= 3:
        print("La nota del alumno {} queda aproximada, su nueva nota es {}".format(i + 1, multiplo))
    elif notas[i] < 40:
        print("El alumno {} mantiene su nota".format(i + 1,notas[i]))
    else:
        pass        
