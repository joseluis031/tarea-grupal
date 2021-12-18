import math
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
