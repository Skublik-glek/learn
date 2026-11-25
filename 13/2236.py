import ipaddress
mask = ipaddress.ip_address("255.255.254.0")
print(f"{mask:b}")
import itertools
comb = itertools.product("01", repeat = 9)
a = 0
for i in comb:
    a = a + 1
    print(i, a)
#из условия от ответа отнять 2(адрес сети(только нули) и широковещательный(только единицы)