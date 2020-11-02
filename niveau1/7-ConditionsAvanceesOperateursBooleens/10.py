nbJetons = int(input())

for jeton in range(nbJetons):
    x = int(input())
    y = int(input())

    if (x < 0 or y < 0 or x > 90 or y > 70):
        print("En dehors de la feuille")
    else:
        if ((x >= 10 and x <= 85 and y >= 10 and y <= 55)
            and not(x >= 25 and x <= 50 and y >= 20 and y <= 45)):
            print("Dans une zone bleue")
        elif (((x >= 15 and x <= 45) or (x >= 60 and x <= 85))
            and (y >= 60 and y <= 70)):
            print("Dans une zone rouge")
        else:
            print("Dans une zone jaune")