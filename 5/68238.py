
for N in range(100, 100000):
    N = str(N)
    b = N[0:3]
    spis = [b]
    d = len(N) - 3
    for a in range(1, d + 1):
        spis.append(N[a:a + 3])
    print(spis, N)

