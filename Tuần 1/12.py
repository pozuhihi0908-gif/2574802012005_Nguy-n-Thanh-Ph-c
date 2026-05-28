def lon_nhat(a):
    max = a[0]
    vitri = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            vitri = i
    return max, vitri
def nho_nhat(a):
    min = a[0]
    vitri = 0
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
            vitri = i
    return min, vitri
a = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in  range(n):
    p = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(p)
max, vitrimax = lon_nhat(a)
min, vitrimin = nho_nhat(a)
print(f"Phần tử lớn nhất trong mảng là {max} ở vị trí {vitrimax}")
print(f"Phần tử nhỏ nhất trong mảng là {min} ở vị trí {vitrimin}")