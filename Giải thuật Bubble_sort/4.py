a = [3, 2, 1]

n = len(a)
swap = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swap += 1

print(a)
print("So lan swap:", swap)