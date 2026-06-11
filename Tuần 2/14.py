def tim_ma_tran(a, x):
    m = len(a)
    n = len(a[0])
    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        hang = mid // n
        cot = mid % n
        if a[hang][cot] == x:
            return True
        elif a[hang][cot] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False
a = [
    [1, 3, 5],
    [7, 9, 11]
]
x = 9
print(tim_ma_tran(a, x))