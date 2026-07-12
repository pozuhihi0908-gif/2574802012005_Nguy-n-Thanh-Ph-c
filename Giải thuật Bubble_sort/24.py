dau = [4, 3, 2, 1]

a = dau.copy()

n = len(a)

pass_count = 0

for i in range(n - 1):

    pass_count += 1

    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

    print("Luot", pass_count, ":", a)