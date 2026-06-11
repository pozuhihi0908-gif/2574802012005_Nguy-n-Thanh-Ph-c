def dau_tien(a, x):
    left = 0
    right = len(a) - 1
    ketqua = -1
    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ketqua = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ketqua
a = [1, 2, 2, 2, 3]
x = 2
print(dau_tien(a, x))