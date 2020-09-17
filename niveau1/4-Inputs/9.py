bas = int(input())
haut = int(input())

total = 0

for i in range(haut, bas + 1):
    total += i * i

print(total)
