import ipaddress
mask = ipaddress.ip_address("255.255.252.0")
print(f"{mask:b}")
ip = ipaddress.ip_address("226.185.90.162")
print(f"{ip:b}")
print(int("1010100010",2))