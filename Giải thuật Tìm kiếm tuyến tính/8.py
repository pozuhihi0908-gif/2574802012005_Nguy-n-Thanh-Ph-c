def dem_xuat_hien(a, x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            dem+= 1
    return dem
a = []
n = int(input("Nhấp số phần tử trong mảng: "))
for i in range(n):
    p = int(input(f"Nhập số phần tử thứ {i+1}: "))
    a.append(p)
x = int(input("Nhập phần tử cần đếm: "))
ketqua = dem_xuat_hien(a, x)
print(f"Phần tử {x} được tìm thấy {ketqua} lần")