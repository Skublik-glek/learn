import itertools

c = 0
for i in range(1, 11):
    for elem in itertools.permutations("0123456789", r=i):
        if elem[0] != "0" and elem[-1] in ("0", "5"):
            c += 1
print(c+1) # +1 это ноль, который не подошёл под общее условие