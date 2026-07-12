a = [2, 4, 1, 3]

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
print("So nghich the =", shift)
print("So shift =", shift)