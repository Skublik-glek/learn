
def from10to2(chis, osnov):
    itog = ""
    while chis >= 1:
        ost = chis % osnov
        itog = str(ost) + itog
        chis = chis // osnov
    return itog
for a in range(1, 10000):
    N = from10to2(a, 3)
    if a % 3 == 0:
        N = N + N[-2:]
    else:
        b = a % 3
        b = b * 5
        b = from10to2(b, 3)
        N = N + b
    N = int(N,3)
    if N <= 173:
        print(N)
