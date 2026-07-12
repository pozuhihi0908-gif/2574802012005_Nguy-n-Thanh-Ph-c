def xuat_hien_cuoi(a, x):
    vitri = -1
    for i in range(len(a)):
        if a[i] == x:
            vitri = i
    return vitri
a = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in  range(n):
    p = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(p)
x = int(input("Nhập số phần tử cần tìm: "))
ketqua = xuat_hien_cuoi(a, x)
if ketqua != -1:
    print(f"Phần tử {x} xuất hiện cuối cùng ở vị trí là: {ketqua}")
else:
   print(f"Không tìm thấy vị trí của phần từ {x}")  
