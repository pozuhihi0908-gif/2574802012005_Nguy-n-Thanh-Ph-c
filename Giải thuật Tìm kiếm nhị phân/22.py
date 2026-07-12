def median_hai_mang(a, b):
    c = a + b
    c.sort()
    n = len(c)
    if n % 2 == 1:
        return c[n // 2]
    else:
        return (c[n // 2 - 1] + c[n // 2]) / 2
a = [1, 3]
b = [2]
print(median_hai_mang(a, b))