dateDebutEtudiee = int(input())
dateFinEtudiee = int(input())

nbInvites = int(input())

nbSuspects = 0

for i in range(nbInvites):
    dateDebutInvite = int(input())
    dateDepartInvite = int(input())

    if (not(dateDepartInvite < dateDebutEtudiee or dateFinEtudiee < dateDebutInvite)):
        nbSuspects += 1

print(nbSuspects)