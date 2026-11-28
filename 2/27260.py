def F(x,y,z,w):
    return ((x or not y) and (not(not z == w)) or(y and z))
print("x,y,z,w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if F(x, y, z, w) == 0:
                    print(x, y, z, w)