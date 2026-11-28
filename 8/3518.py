import itertools


comb = itertools.product("АМРТ",repeat=4)
a = 0
for i in comb:
    a = a + 1
    print(a,i)