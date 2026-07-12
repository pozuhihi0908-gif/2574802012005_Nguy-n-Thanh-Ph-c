a = [1, 2, 3, 4]

n = len(a)
pass_count = 0

for i in range(n - 1):
    swapped = False
    pass_count += 1

    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True

    if swapped == False:
        break

print(pass_count)