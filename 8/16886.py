import itertools


comb = itertools.permutations("матвей",r = 6)
a = 0
for i in comb:
    i = "".join(i)
    if i[0] != "й" and "ае" not in i:
       a = a + 1
print(a)