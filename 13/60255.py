import ipaddress
mask = ipaddress.ip_address("255.255.255.240")
print(f"{mask:b}")
ip = ipaddress.ip_address("192.168.32.160")
print(f"{ip:b}")
network = ipaddress.ip_network("192.168.32.160/255.255.255.240", strict=False)
for i in network:
    if f"{i:b}".count("1") % 2 == 0:
        print(i)
#для решения задач с перебором по условию(например, для подсета чет/нечет единиц)