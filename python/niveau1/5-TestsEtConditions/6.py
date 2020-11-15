de1 = int(input())
de2 = int(input())

somme = de1 + de2

if (somme >= 10):  
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(somme * 2)
