a = [1, 2, 3]

n = len(a)
compare = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        compare += 1
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
print("So lan so sanh:", compare)