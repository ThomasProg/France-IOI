numRecherche = int(input())

tailleListe = int(input())

estDansLaVille = True

for i in range(tailleListe):
    num = int(input())

    if (num == numRecherche):
        estDansLaVille = False

if (estDansLaVille):
    print("Encore dans la ville")
else:
    print("Sorti de la ville")