def dat_duoc_nam_cham(x, m, khoang_cach):
    dem = 1
    vi_tri_cuoi = x[0]
    for i in range(1, len(x)):
        if x[i] - vi_tri_cuoi >= khoang_cach:
            dem += 1
            vi_tri_cuoi = x[i]
    return dem >= m
def magnetic_force(x, m):
    x.sort()
    left = 1
    right = x[-1] - x[0]
    ketqua = 0
    while left <= right:
        mid = (left + right) // 2
        if dat_duoc_nam_cham(x, m, mid):
            ketqua = mid
            left = mid + 1
        else:
            right = mid - 1
    return ketqua
x = [1, 2, 3, 4, 7]
m = 3
print(magnetic_force(x, m))