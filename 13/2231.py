import ipaddress

mask = ipaddress.ip_address("255.255.255.224")
print(f"{mask:b}")
ip = ipaddress.ip_address("162.198.0.157")
print(f"{ip:b}")
print(int("11101",2))

network = ipaddress.ip_network("162.198.0.157/255.255.255.224", strict=False)
ip = ipaddress.ip_address("162.198.0.157")
print(int(ip) - int(network.network_address))