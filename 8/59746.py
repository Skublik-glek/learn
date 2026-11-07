import itertools


a = 0
for j in range (1,11):
    comb = itertools.permutations("0123456789",r=j)
    for i in comb:
        if i[0] != "0":
            i = "".join(i)
            i = int(i)
            if i % 5 == 0:
                a += 1
print(a+1)