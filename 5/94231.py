for N in range(1000, 0, -1):
    a = f"{N:b}"
    if N % 2 == 0:
        a = "10" + a
    else:
        a = "1" + a + "01"
    R = a
    R = int(R, 2)
    if R <= 80:
        print(N,R)
        break