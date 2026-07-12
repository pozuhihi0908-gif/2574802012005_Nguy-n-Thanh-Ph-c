arr = [1, 2, 3, 4, 5, 6]

i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        arr.pop(i)
    else:
        i = i + 1

print(arr)