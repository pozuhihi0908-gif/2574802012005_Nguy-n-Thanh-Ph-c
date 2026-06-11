def co_the_ship(w, d, suc_chua):
    ngay = 1
    tong = 0
    for i in range(len(w)):
        if tong + w[i] <= suc_chua:
            tong += w[i]
        else:
            ngay += 1
            tong = w[i]
    return ngay <= d
def ship_hang(w, d):
    left = max(w)
    right = sum(w)
    ketqua = right
    while left <= right:
        mid = (left + right) // 2
        if co_the_ship(w, d, mid):
            ketqua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ketqua
w = [1,2,3,4,5,6,7,8,9,10]
d = 5
print(ship_hang(w, d))