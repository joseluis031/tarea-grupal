# tarea-grupal
Nuestra dirección de github es: [Github](https://github.com/joseluis031/tarea-grupal.git)

# 1.Ejercicio simple de la suma de una matriz

Dada una matriz de números enteros N, tenemos que hacer la suma de sus elementos.

El diagrama de flujos es el siguiente:

![suma matriz simple](https://user-images.githubusercontent.com/91721888/146649137-90fd8964-6c55-4235-b87b-7aadb7fd8197.png)


El código de la suma simple de la matriz es el siguiente:
```

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
```

```
# 3.Ejercicio: Una suma muy grande

En este desafío, debe calcular e imprimir la suma de los elementos en una matriz, teniendo en cuenta
que algunos de esos números enteros pueden ser bastante grandes.

El diagrama de flujos es el siguiente:

![suma grande matriz](https://user-images.githubusercontent.com/91721888/146649189-f3188b6d-3ca5-4205-bf0f-c8036d9809ac.png)


El código de una suma muy grande es:
```

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


El código de la esclaera es:
```

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
```

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
```

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
```

```


