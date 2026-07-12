def chia_duoc(a, k, gioi_han):
    doan = 1
    tong = 0
    for i in range(len(a)):
        if tong + a[i] <= gioi_han:
            tong += a[i]
        else:
            doan += 1
            tong = a[i]
    return doan <= k
def split_array(a, k):
    left = max(a)
    right = sum(a)
    ketqua = right
    while left <= right:
        mid = (left + right) // 2
        if chia_duoc(a, k, mid):
            ketqua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ketqua
a = [7, 2, 5, 10, 8]
k = 2
print(split_array(a, k))