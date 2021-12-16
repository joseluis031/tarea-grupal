import math
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