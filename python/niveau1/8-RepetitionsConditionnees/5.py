
nbTotalMesures = int(input())
tempMin = int(input())
tempMax = int(input())

doitContinuer = True

count = 0

while (doitContinuer):
    tempActu = int(input())
    count += 1

    if (tempActu >= tempMin and tempActu <= tempMax):
        print("Rien à signaler")
    else:
        print("Alerte !!")
        doitContinuer = False

    if (count >= nbTotalMesures):
        doitContinuer = False