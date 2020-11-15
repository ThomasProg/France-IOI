nbPaires = int(input())

for paire in range(nbPaires):
    # 1er rectangle
    xMin1 = int(input())
    xMax1 = int(input())
    yMin1 = int(input())
    yMax1 = int(input())

    # 2e rectangle
    xMin2 = int(input())
    xMax2 = int(input())
    yMin2 = int(input())
    yMax2 = int(input())

    if (not(xMax1 <= xMin2 or xMax2 <= xMin1) and not(yMax1 <= yMin2 or yMax2 <= yMin1)):
        print("OUI")
    else:
        print("NON")