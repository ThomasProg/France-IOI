from math import *

nbPopActu = int(input())
croissance = float(input()) / 100

print(floor(nbPopActu + nbPopActu * croissance))