nbVariations = int(input())

altMontee = 0
altDescendue = 0

for i in range(nbVariations):
    varAltitude = int(input())
    if (varAltitude < 0):
        altDescendue -= varAltitude
    else:
        altMontee += varAltitude

print(altMontee)
print(altDescendue)