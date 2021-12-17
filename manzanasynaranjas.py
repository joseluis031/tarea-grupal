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