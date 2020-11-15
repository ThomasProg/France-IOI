nbPersonnes = int(input())

maxNbSimultanees = 0

nbSimulanees = 0

for i in range(nbPersonnes * 2):
    n = int(input())
    if (n > 0):
        nbSimulanees += 1
    else:
        maxNbSimultanees = max(maxNbSimultanees, nbSimulanees)
        nbSimulanees -= 1

    


print(maxNbSimultanees)