from robot import *

for i in range(1, 11):
    for j in range(i):
        droite()
    ramasser()
    for j in range(i):
        gauche()
    deposer()