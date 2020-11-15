positionDepart = int(input())
largeurEmplacement = int(input())
nbVendeurs = int(input())

for i in range(nbVendeurs + 1):
    print(positionDepart + largeurEmplacement * i)