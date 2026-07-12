def can_bac_hai(n):
    left = 0
    right = n
    ketqua = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ketqua = mid
            left = mid + 1
        else:
            right = mid - 1
    return ketqua
n = 8
print(can_bac_hai(n))