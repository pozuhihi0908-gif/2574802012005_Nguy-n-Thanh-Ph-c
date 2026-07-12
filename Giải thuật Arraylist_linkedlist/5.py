arr = [1, 2, 3, 4]

dem = 0

for i in range(len(arr)):
    print(arr[i])
    if arr[i] % 2 == 0:
        dem = dem + 1

print("Số chẵn:", dem)