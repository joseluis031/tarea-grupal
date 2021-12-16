from random import randint

nota1 = randint(0,10)
nota2 = randint(0,10)
nota3 = randint(0,10)

nota4 = randint(0,10)
nota5 = randint(0,10)
nota6 = randint(0,10)

print("Las notas de Lucía son:\nClaridad del problema = {} \nOriginalidad = {} \nDificultad = {}".format(nota1,nota2,nota3))
print("Las notas de Carlos son:\nClaridad del problema = {} \nOriginalidad = {} \nDificultad = {}".format(nota4,nota5,nota6))


def comparar_Notas():
    nota_total_Lucia = 0
    nota_total_Carlos = 0
    a = [nota1,nota2,nota3]
    b = [nota4,nota5,nota6]
    if a[0] > b[0]:
        nota_total_Lucia += 1
    elif a[0] < b[0]:
        nota_total_Carlos += 1
    else:
        pass
    
    if a[1] > b[1]:
        nota_total_Lucia += 1
    elif a[1] < b[1]:
        nota_total_Carlos += 1
    else:
        pass
    
    if a[2] > b[2]:
        nota_total_Lucia += 1
    elif a[2] < b[2]:
        nota_total_Carlos += 1
    else:
        pass
    c = nota1 + nota2 + nota3
    d = nota4 + nota5 + nota6
    print("La nota total de lucía es:", c)
    print("La nota total de Carlos es:", d)
    
    if c > d:
        print("Lucía tiene mas nota")
    elif c < d:
        print("Carlos tiene mas nota")
    else:
        print("Tienen la misma nota")
comparar_Notas()


