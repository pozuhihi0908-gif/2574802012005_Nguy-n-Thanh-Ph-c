a = [5, 2, 4, 6, 1, 3]

n = len(a)

compare = 0
shift = 0

for i in range(1, n):

    key = a[i]
    j = i - 1

    while j >= 0:

        compare += 1

        if a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shift += 1
        else:
            break

    a[j + 1] = key

print(a)
print("So sanh:", compare)
print("Shift:", shift)