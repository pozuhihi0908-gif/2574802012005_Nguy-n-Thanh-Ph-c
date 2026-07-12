arr = [100,4,200,1,3,2]

tap = {}

for i in arr:
    tap[i] = True

lonnhat = 0

for i in arr:

    if i-1 not in tap:

        dem = 1

        x = i

        while x+1 in tap:
            dem = dem + 1
            x = x + 1

        if dem > lonnhat:
            lonnhat = dem

print(lonnhat)