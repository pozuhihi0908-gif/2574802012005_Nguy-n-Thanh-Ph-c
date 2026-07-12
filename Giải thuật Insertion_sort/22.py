a = [2, 1, 3, 5, 4]

n = len(a)

shift = 0

for i in range(1, n):

    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        shift += 1

    a[j + 1] = key

print(a)
print("So shift:", shift)   