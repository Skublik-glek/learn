def F(x, y, z, w):
    return ((not y or x) == (not x or w)) and (z or x)
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if F(x, y, z, w) == 1:
                    print(x, y, z, w)