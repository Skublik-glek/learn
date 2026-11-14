for N in range(1,1000):
    a = N
    if N % 2 == 0:
        N = bin(N) + "00"
    else:
        N = bin(N) + "11"
    N = int(N,2)
    if N > 115:
        print(a)
        break 