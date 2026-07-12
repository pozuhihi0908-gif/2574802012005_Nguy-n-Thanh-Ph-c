arr = [5, 3, 7]

x = 7
tim = -1

for i in range(len(arr)):
    if arr[i] == x:
        tim = i
        break

print(tim)