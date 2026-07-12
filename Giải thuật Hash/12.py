arr = [1,1,1]

k = 2

tong = 0

dem = 0

bang = {}

bang[0] = 1

for i in arr:

    tong = tong + i

    if tong - k in bang:
        dem = dem + bang[tong-k]

    if tong in bang:
        bang[tong] = bang[tong] + 1
    else:
        bang[tong] = 1

print(dem)