a = [1, 2, 3]

n = len(a)

compare = 0

for i in range(1, n):

    key = a[i]
    j = i - 1

    while j >= 0:

        compare += 1

        if a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        else:
            break

    a[j + 1] = key

print(a)
print("So lan so sanh:", compare)