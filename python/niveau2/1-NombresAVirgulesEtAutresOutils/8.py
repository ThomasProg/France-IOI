from math import *

taxeActuelle = float(input()) / 100
nouvelleTaxe = float(input()) / 100
prixLegume = float(input())

prixSansTaxe = prixLegume / (1 + taxeActuelle) 
prixNouvelleTaxe = prixSansTaxe * (1 + nouvelleTaxe)

print(round(prixNouvelleTaxe * 100) / 100)