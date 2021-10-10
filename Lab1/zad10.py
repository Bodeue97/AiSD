def zad10(napis):
    a = True
    for x in range(len(napis)):
        if napis[x] != napis[-x-1]:
            a = False

    return a

print(zad10("kajak"))
print(zad10("słowo"))



