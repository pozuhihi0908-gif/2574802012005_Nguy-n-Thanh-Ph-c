a = [5, 1, 4, 2, 8]

n = len(a)

swap = 0
compare = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        compare += 1

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swap += 1

print(a)
print("So lan so sanh:", compare)
print("So lan swap:", swap)