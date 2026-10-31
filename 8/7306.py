import itertools


comb = itertools.product("ученик",repeat=5)
a = 0
for i in comb:
    if i[0] =="у" and i[4] == "к":
        a = a + 1
print(a)
