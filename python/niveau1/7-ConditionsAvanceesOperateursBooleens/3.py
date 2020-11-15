
numMois = int(input())

if (numMois == 11):
    print(29)
elif ((numMois >= 4 and numMois <= 6) or numMois == 10):
    print(31)
else:
    print(30)
