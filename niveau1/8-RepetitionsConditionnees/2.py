somme = 0
doitContinuer = True
while (doitContinuer):
    valeur = int(input())
    if (valeur == -1):
        doitContinuer = False
    else:
        somme += valeur 

print(somme)