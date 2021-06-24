nbMaxPierres = int(input())

cote = 0
nbPierresActu = 0

while (nbPierresActu <= nbMaxPierres):
    cote += 1
    nbPierresActu += cote * cote

nbPierresActu -= cote * cote
cote -= 1

print(cote)
print(nbPierresActu)
