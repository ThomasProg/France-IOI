
popTotale = int(input())
nbMalades = 1
jour = 1

while (nbMalades < popTotale):
    nbMalades *= 3
    jour += 1

print(jour)