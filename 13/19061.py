import ipaddress
ip = ipaddress.ip_address("111.81.27.224")
print(f"{ip:b}")
address = ipaddress.ip_address("111.81.27.192")
print(f"{address:b}")
mask = 26 * "1" + "000000"
mask = ipaddress.IPv4Address(int('11111111111111111111111111000000', 2))
print(mask)