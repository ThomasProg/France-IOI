nbMembres = int(input())

poidsTotal1 = 0
poidsTotal2 = 0

for i in range(nbMembres):
    poidsTotal1 += int(input())
    poidsTotal2 += int(input())

if (poidsTotal1 > poidsTotal2):
    print("L'équipe 1 a un avantage")
elif (poidsTotal2 > poidsTotal1):
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 : ", poidsTotal1)
print("Poids total pour l'équipe 2 : ", poidsTotal2)