nbMarchands = int(input())

prixMin = int(input())
pos = 1

for posMarchand in range(2, nbMarchands + 1):
    prixGalettes = int(input())
    if (prixGalettes <= prixMin):
        prixMin = prixGalettes
        pos = posMarchand

print(pos)