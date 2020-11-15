heureArrivee = int(input())

prixChambre = 10 + 5 * heureArrivee

if (prixChambre > 53):
    prixChambre = 53

print(prixChambre)