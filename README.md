# tarea-grupal
Nuestra dirección de github es: [Github](https://github.com/joseluis031/tarea-grupal.git)

# 1.Ejercicio simple de la suma de una matriz

Dada una matriz de números enteros N, tenemos que hacer la suma de sus elementos.

El diagrama de flujos es el siguiente:

![suma matriz simple](https://user-images.githubusercontent.com/91721888/146649137-90fd8964-6c55-4235-b87b-7aadb7fd8197.png)


El código de la suma simple de la matriz es el siguiente:
```import random

matriz = [
    [random.randint(0,10),random.randint(0,10)],
    [random.randint(0,10),random.randint(0,10)]
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

```
# 2.Ejercicio: Compara los problemas

Lucía y Carlos crearon cada uno un problema para su posterior calificación.
Un revisor califica los dos problemas, otorgando puntos en una escala del 1 al 100 para tres 
categorías: claridad del problema, originalidad y dificultad .
La calificación del desafío de Lucía es el desafío a = (a [0], a [1], a [2]), y la calificación del desafío de 
Carlos es el desafío b = (b [0], b [1], b [2]) .
La tarea consiste en encontrar sus puntos de comparación comparando a [0] con b [0] , a [1] con b
[1] y a [2] con b [2] .
Si a [i]> b [i] , entonces Lucía recibe 1 punto.
Si a [i] <b [i] , entonces Carlos recibe 1 punto.
Si a [i] = b [i] , ninguna persona recibe un punto.
Los puntos de comparación son los puntos totales que ganó una persona.
Dada una a y b , determinar sus respectivos puntos de comparación.
Para los elementos * 0 *, Carlos recibe un punto debido a un [0].
Para los elementos iguales a [1] y b [1] , se consiguen sin puntos.
Finalmente, para los elementos 2 , a [2]> b [2] por lo que Lucía recibe un punto.
La matriz de retorno es [1, 1] con la puntuación de Lucía primero y la de Carlos en segundo lugar.

El diagrama de flujos es el siguiente:

![figma comparar notas](https://user-images.githubusercontent.com/91721888/146649175-667df933-27a0-44d8-bbfb-3ca2f6b4e77d.png)


El código de comparar los problemas es:
```from random import randint

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



```
# 3.Ejercicio: Una suma muy grande

En este desafío, debe calcular e imprimir la suma de los elementos en una matriz, teniendo en cuenta
que algunos de esos números enteros pueden ser bastante grandes.

El diagrama de flujos es el siguiente:

![suma grande matriz](https://user-images.githubusercontent.com/91721888/146649189-f3188b6d-3ca5-4205-bf0f-c8036d9809ac.png)


El código de una suma muy grande es:
```import random

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

```
# 4.Ejercicio: La escalera
Esta es una escalera de tamaño n:
 #
 ##
###
####
Su base y altura son iguales a n. Se dibuja mediante #símbolos y espacios. La última línea no está
precedida por espacios.
Escribe un programa que imprima una escalera de tamaño n.

El diagrama de flujos es el siguiente:

![figma escalera](https://user-images.githubusercontent.com/91721888/146649222-6109df5a-2805-43cf-b55d-792c59e57f6b.png)


El código de la escalera es:
```import math
import os
import random
import re
import sys
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
def escalera(n):
    for i in range(0, n):
        linea = ""
        for k in range(0,1-i):
            linea = linea + ""
        for j in range(0,i + 1):
            linea = linea + "€"
        print(linea)

if __name__ == '__main__':
   n = int(input("Introduce las dimensiones que desees de la escalera:").strip())
escalera(n)

```
# 5.Ejercicio: Juego de las piedras
Dos jugadores llamados P1 Y P2 están jugando un juego con un número inicial de n piedras. Jugador1 
siempre juega primero, y los dos jugadores se mueven en turnos alternos. Las reglas del juego son las 
siguientes:
En un solo movimiento, un jugador puede eliminar ,2,3 o 5 , o piedras del tablero de juego.
Si un jugador no puede hacer un movimiento, ese jugador pierde el juego.
Dado el número inicial de piedras, busque e imprima el nombre del ganador.
Cada jugador juega de manera óptima, lo que significa que no harán un movimiento que les haga perder 
el juego si existe un movimiento ganador.
• Por ejemplo, si n=4, P1 puede hacer los siguientes movimientos:
• P1 elimina 2 piedras quedando 2. P2 luego eliminará 2 piedras y ganar.
• P1 elimina 3 piedras quedando 1 . P2 no se puede mover y pierde.

El diagrama de flujos es el siguiente:

![figma piedras](https://user-images.githubusercontent.com/91721888/146649230-90e5d8dc-c494-402d-bcff-ad58020d4f8a.png)


El código del juego de las piedras es el siguiente:
```import random

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
    

```
# 6.Ejercicio: Rana en laberinto
La rana Alef está en un laberinto bidimensional nxm representado como una mesa. El laberinto tiene las 
siguientes características:
• Cada celda puede ser libre o contener un obstáculo, una salida o una mina .
• Dos celdas cualesquiera de la tabla se consideran adyacentes si comparten un lado.
• El laberinto está rodeado por una pared sólida hecha de obstáculos.
• Algunos pares de celdas libres están conectados por un túnel bidireccional.
• Cuando Alef está en cualquier celda, puede elegir al azar y con la misma probabilidad moverse 
a una de las celdas adyacentes que no contengan ningún obstáculo. Si esta celda contiene una 
mina, la mina explota y Alef muere. Si esta celda contiene una salida, Alef escapa del laberinto.
• Cuando Alef aterriza en una celda con una entrada a un túnel, es inmediatamente transportado 
a través del túnel y arrojado a la celda en el otro extremo del túnel. A partir de entonces, no 
volverá a caer y ahora volverá a moverse aleatoriamente a una de las celdas 
adyacentes. (Posiblemente podría caer en el mismo túnel más tarde).
• Es posible que Alef se quede atascado en el laberinto en el caso de que la celda en la que fue 
arrojado desde un túnel esté rodeada de obstáculos por todos lados.
• Su tarea es escribir un programa que calcule e imprima una probabilidad de que Alef escape del 
laberinto.

El diagrama de flujos es el siguiente:

![figma rana](https://user-images.githubusercontent.com/91721888/146649237-5ef5af91-a4a5-4c34-ac3f-e1a9864106c0.png)


El código de la rana es el siguiente:
```

```
# 7.Ejercicio: Estudiantes de calificación
La Universidad para el nuevo curso va a implementar una nueva poítica de calificación:
• Cada estudiante recibe una nota en el rango inclusivo de 0 a 100 .
• Si tienes una nota inferior a 40 o menos es una calificación suspensa.
Además a los profesores en la universidad nos gusta redondear los de acuerdo con estas reglas:
• Si la diferencia entre una nota y el siguiente múltiplo de es menos que 3 , se redondea hasta el 
siguiente múltiplo de 5 .
• Si el valor de la nota es menorque 40 , no se produce redondeo ya que el resultado seguirá 
siendo una calificación suspensa.
Ejemplos
• 84 redondear a (85 - 84 es menos de 3)
• 29 no redondear (el resultado es menos de 40)
• 57 no redondear (60 - 57 es 3 o más)
Dado el valor inicial de la nota para cada uno de los n estudiantes, escriban código para automatizar 
el proceso de redondeo

El diagrama de flujos es el siguiente;

![figma calificaciones estudiantes](https://user-images.githubusercontent.com/91721888/146649244-50be06a1-26d3-4151-b02c-b562c522f0bb.png)


El código de estudiantes de calificación es:
```notas = [73,67,38,33]

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

```
# 8. Ejercicio: Manzana y naranja
La casa de Sam tiene un manzano y un naranjo que dan frutos en abundancia. Con la información que se 
proporciona a continuación, determine la cantidad de manzanas y naranjas que aterrizan en la casa de 
Sam.
En el diagrama siguiente:
La región roja denota la casa, s donde es el punto de inicio, y t es el punto final. El manzano está a la 
izquierda de la casa y el naranjo está a la derecha.
Suponga que los árboles están ubicados en un solo punto, donde el manzano está en el puntoa , y el 
naranjo está en el punto b .
Cuando una fruta cae de su árbol, aterriza a d unidades de distancia desde su árbol de origen a lo 
largo del eje x. * Un valor negativo de significa que la fruta cayó a d unidades a la izquierda del 
árbol, y un valor positivo de significa que cae a d unidades a la derecha del árbol. *
Dado el valor de d por m manzanas y n naranjas, determine cuántas manzanas y naranjas caerán en la 
casa de Sam (es decir, en el rango inclusivo )

El diagrama de flujos es el siguiente:



El código de la manzana y la naranja es el siguiente:
```import math
import os
import random
import re
import sys

def contador(a, b, c, d, manzanas, naranjas):
    manzanas_en_caja = 0
    naranjas_en_caja = 0
    for manzana in manzanas:
        if(c+manzana >= a and c+manzana <= b):
            manzanas_en_caja +=1
    for naranja in naranjas:
        if(d+naranja >= a and d+naranja <= b):
            naranjas_en_caja +=1
    print("Han caido " +str(manzanas_en_caja) + " manzanas dentro")
    print("Han caido " + str(naranjas_en_caja) + " naranjas dentro")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
a = int(first_multiple_input[0])
b = int(first_multiple_input[1])
second_multiple_input = input().rstrip().split()
c = int(second_multiple_input[0])
d = int(second_multiple_input[1])
third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

manzanas = list(map(int, input().rstrip().split()))
naranjas = list(map(int, input().rstrip().split()))
contador(a, b, c, d, manzanas, naranjas)

```


