a = [3, 2, 1]
k = 1

n = len(a)

for i in range(k):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

ok = True

for i in range(n - 1):
    if a[i] > a[i + 1]:
        ok = False

print(ok)