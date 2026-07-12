a = [3, 2, 1]

n = len(a)

i = 0

while i < n:

    if i == 0:
        i += 1

    elif a[i] >= a[i - 1]:
        i += 1

    else:
        a[i], a[i - 1] = a[i - 1], a[i]
        i -= 1

print(a)