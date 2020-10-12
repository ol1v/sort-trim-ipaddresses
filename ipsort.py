ipaddresses = []
with open("ipaddresses.txt") as ip:
    for line in ip:
        if line not in ipaddresses:
            ipaddresses.append(line)

ipaddresses = list(dict.fromkeys(ipaddresses))

for ip in ipaddresses:
    print(ip)

