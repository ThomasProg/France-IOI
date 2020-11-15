nbJoursMarche = int(input())

distMax = 0

for i in range(nbJoursMarche):
    distJour = int(input())
    if (distMax < distJour):
        distMax = distJour

print(distMax)