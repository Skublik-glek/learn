import itertools


comb = itertools.product("АОУ",repeat=5)
a = 0
for i in comb:
    a = a + 1
    print(i, a)