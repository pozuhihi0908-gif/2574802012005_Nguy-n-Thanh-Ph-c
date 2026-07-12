arr = ["a","b","a","c","a"]

dem = {}

for i in arr:

    if i in dem:
        dem[i] = dem[i] + 1
    else:
        dem[i] = 1

print(dem)