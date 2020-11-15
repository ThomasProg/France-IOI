from robot import *

for i in range(9):
    haut()

for j in range(4):  
    droite()
    for i in range(8):
        bas()
    droite()
    for i in range(8):
        haut()

droite()
for i in range(9):
    bas()

for i in range(9):
    gauche()