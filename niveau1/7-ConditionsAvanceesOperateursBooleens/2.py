xMin = int(input())
xMax = int(input())

yMin = int(input())
yMax = int(input())

nbMaisons = int(input())

nbMaisonsDansZone = 0

for i in range(nbMaisons):
    x = int(input())
    y = int(input())

    if (x >= xMin and x <= xMax and y >= yMin and y <= yMax):
        nbMaisonsDansZone += 1

print(nbMaisonsDansZone)