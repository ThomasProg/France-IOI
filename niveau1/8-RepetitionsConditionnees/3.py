doitContinuer = True
nbATrouver = int(input())
nbEssais = 0

while (doitContinuer):
    nbDuJoueur = int(input())
    nbEssais += 1
    if (nbDuJoueur == nbATrouver):
        doitContinuer = False 
    elif (nbDuJoueur > nbATrouver):
        print("c'est moins")
    else:
        print("c'est plus")

print("Nombre d'essais nécessaires :")
print(nbEssais)