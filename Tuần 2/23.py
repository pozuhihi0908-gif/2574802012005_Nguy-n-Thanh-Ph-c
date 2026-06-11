def dem_nho_hon(matrix, gia_tri):
    dem = 0
    n = len(matrix)
    hang = n - 1
    cot = 0
    while hang >= 0 and cot < n:
        if matrix[hang][cot] <= gia_tri:
            dem += hang + 1
            cot += 1
        else:
            hang -= 1
    return dem
def kth_smallest(matrix, k):
    n = len(matrix)
    left = matrix[0][0]
    right = matrix[n - 1][n - 1]
    while left < right:
        mid = (left + right) // 2
        if dem_nho_hon(matrix, mid) < k:
            left = mid + 1
        else:
            right = mid
    return left
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(kth_smallest(matrix, k))