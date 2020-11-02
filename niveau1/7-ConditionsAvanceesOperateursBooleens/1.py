debut = int(input())
fin = int(input())

nbEntrees = int(input())

nbPersonnesSuspectes = 0

for i in range(nbEntrees):
    dateEntree = int(input())

    if (dateEntree >= debut and dateEntree <= fin):
        nbPersonnesSuspectes += 1

print(nbPersonnesSuspectes)
