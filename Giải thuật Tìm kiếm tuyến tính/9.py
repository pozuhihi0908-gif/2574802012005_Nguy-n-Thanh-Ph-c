def tim_tat_ca(a, x):
    vitri = []
    for i in range(len(a)):
        if a[i] == x:
            vitri.append(i)
    return vitri
a = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in range(n):
    p = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(p)
x = int(input("Nhập số phần tử cần tìm vị trí: "))
ketqua = tim_tat_ca(a, x)
print(f"Phần tử {x} được tìm thấy ở các vị trí {ketqua}")