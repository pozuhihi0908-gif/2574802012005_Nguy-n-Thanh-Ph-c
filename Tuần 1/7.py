def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False
a = []
x = int(input("Nhập giá trị cần tìm: "))
n = int(input("Nhấp số phần tử của mảng: "))
for i in range(n):
    p = int(input(f"Nhấp số phần tử thứ {i+1}: "))
    a.append(p)
ketqua = ton_tai(a, x)
print(ketqua)
