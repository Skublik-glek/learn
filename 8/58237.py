import itertools


comb = itertools.permutations([0,1,2,3,4,5,6],r=4)
a = 0
for i in comb:
    if i[0] > i[1] > i[2] > i[3] and i[0] != 0:
        a += 1
        print(i)
print(a)