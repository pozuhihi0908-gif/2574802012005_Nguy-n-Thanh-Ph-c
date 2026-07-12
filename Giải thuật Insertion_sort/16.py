a = [5, 2, 8, 1]

b = []

for x in a:

    b.append(x)

    i = len(b) - 2

    while i >= 0 and b[i] > x:
        b[i + 1] = b[i]
        i -= 1

    b[i + 1] = x

    print(b)