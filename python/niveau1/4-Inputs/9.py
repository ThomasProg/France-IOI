volumeSocle = 0

largeurSocleMax = int(input())
largeurSocleMin = int(input())

for largeurEtage in range(largeurSocleMin, largeurSocleMax + 1):
    volumeEtage = 1 * largeurEtage * largeurEtage
    volumeSocle += volumeEtage

print(volumeSocle)