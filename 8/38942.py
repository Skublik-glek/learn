import itertools


comb = itertools.product("АВОРТ",repeat=4)
a = 0
for i in comb:
    a = a + 1
    if ("В","А","Т","А") == i:
        print(i, a)