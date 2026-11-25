import ipaddress
ip = ipaddress.ip_address("98.162.71.94")
print(f"{ip:b}")
network_address = ipaddress.ip_address("98.162.71.64")
print(f"{network_address:b}")
print(int("111111", 2))