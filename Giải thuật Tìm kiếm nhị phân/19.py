def dat_duoc_bo(x, c, khoangcach):
    dem = 1
    vi_tri_cuoi = x[0]
    for i in range(1, len(x)):
        if x[i] - vi_tri_cuoi >= khoangcach:
            dem += 1
            vi_tri_cuoi = x[i]
    return dem >= c
def aggressive_cows(x, c):
    x.sort()
    left = 1
    right = x[-1] - x[0]
    ketqua = 0
    while left <= right:
        mid = (left + right) // 2
        if dat_duoc_bo(x, c, mid):
            ketqua = mid
            left = mid + 1
        else:
            right = mid - 1
    return ketqua
x = [1, 2, 4, 8, 9]
c = 3
print(aggressive_cows(x, c))