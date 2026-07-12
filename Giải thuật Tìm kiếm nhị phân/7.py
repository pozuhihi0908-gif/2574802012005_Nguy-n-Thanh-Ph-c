def upper_bound(a, x):
    left = 0
    right = len(a) - 1
    ketqua = len(a)
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            ketqua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ketqua
a = [1, 3, 5, 7]
x = 5
print(upper_bound(a, x))