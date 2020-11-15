nbPersonnesConsiderees = int(input())

for i in range(nbPersonnesConsiderees):
    taille = int(input())
    age = int(input())
    poids = int(input())
    possedeCheval = int(input())
    estBrun = int(input())

    criteres = 0
    if (taille >= 178 and taille <= 182):
        criteres += 1

    if (age >= 34):
        criteres += 1

    if (poids < 70):
        criteres += 1

    if (possedeCheval == 0):
        criteres += 1

    if (estBrun == 1):
        criteres += 1

    if (criteres == 5):
        print("Très probable")
    elif (criteres == 4 or criteres == 3):
        print("Probable")
    elif (criteres == 0):
        print("Impossible")
    else:
        print("Peu probable")

