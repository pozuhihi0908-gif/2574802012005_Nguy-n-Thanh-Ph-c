servers = [10,30,50]

keys = [5,18,35,60]

for key in keys:

    server = servers[0]

    for s in servers:

        if s >= key:
            server = s
            break

    print(key,"->",server)

print()

servers.append(40)

servers.sort()

for key in keys:

    server = servers[0]

    for s in servers:

        if s >= key:
            server = s
            break

    print(key,"->",server)