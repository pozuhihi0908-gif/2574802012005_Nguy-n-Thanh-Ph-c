def chia_duoc_sach(p, m, gioi_han):
    hoc_sinh = 1
    tong = 0
    for i in range(len(p)):
        if tong + p[i] <= gioi_han:
            tong += p[i]
        else:
            hoc_sinh += 1
            tong = p[i]
    return hoc_sinh <= m
def book_allocation(p, m):
    left = max(p)
    right = sum(p)
    ketqua = right
    while left <= right:
        mid = (left + right) // 2
        if chia_duoc_sach(p, m, mid):
            ketqua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ketqua
p = [12, 34, 67, 90]
m = 2
print(book_allocation(p, m))