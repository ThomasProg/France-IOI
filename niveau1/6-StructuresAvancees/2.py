posActu = int(input())

nbVillages = int(input())

nbVillagesProches = 0

for i in range(nbVillages):
    posVillage = int(input())
    diff = posActu - posVillage
    if (diff <= 50 and diff >= -50):
        nbVillagesProches += 1


print(nbVillagesProches)