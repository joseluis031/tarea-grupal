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
    
    if nota1 > nota4:
        nota_total_Lucia += 1
    elif nota1 < nota4:
        nota_total_Carlos += 1
    else:
        pass
    
    if nota2 > nota5:
        nota_total_Lucia += 1
    elif nota2 < nota5:
        nota_total_Carlos += 1
    else:
        pass
    
    if nota3 > nota6:
        nota_total_Lucia += 1
    elif nota3 < nota6:
        nota_total_Carlos += 1
    else:
        pass