def lon_nhat(a):
    max = a[0]
    vitri = []
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        vitri = i
    return max, vitri
a = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in  range(n):
    p = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(p)
max, vitrimax = lon_nhat(a)
print(f"Phần tử lớn nhất trong mảng là {max} ở vị trí {vitrimax}")