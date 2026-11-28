import ipaddress
from ipaddress import ip_address

mask = ipaddress.ip_address("255.255.254.0")
print(f"{mask:b}")
ip = ipaddress.ip_address("127.204.113.250")
print(f"{ip:b}")
spis = "01111111 11001100 01110000 00000001".split()
for i in spis:
    print(int(i, 2),end = ".")
#ip = ipaddress.IPv4Address(int('11000000101010000000000100000001', 2)) - второй вариант решения

