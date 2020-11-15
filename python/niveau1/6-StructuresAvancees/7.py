nbMaisons = int(input())

xMin = 1000000
yMin = 1000000
xMax = 0
yMax = 0

for maison in range(nbMaisons):
    x = int(input())
    y = int(input())

    if (x < xMin):
        xMin = x 
    if (x > xMax):
        xMax = x

    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y

print(2 * (xMax - xMin + yMax - yMin))
