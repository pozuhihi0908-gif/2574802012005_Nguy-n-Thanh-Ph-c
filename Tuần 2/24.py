def can_them_tram(x, khoang_cach):
    tram_moi = 0
    for i in range(1, len(x)):
        tram_moi += int((x[i] - x[i - 1]) / khoang_cach)
    return tram_moi
def gas_station(x, k):
    left = 0
    right = x[-1] - x[0]
    while right - left > 0.000001:
        mid = (left + right) / 2
        if can_them_tram(x, mid) > k:
            left = mid
        else:
            right = mid
    return right
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
print(gas_station(x, k))