nbLieux = int(input())

nbVilles = 0 

for i in range(nbLieux):
    nbHabs = int(input())
    if (nbHabs > 10000):
        nbVilles += 1

print(nbVilles)