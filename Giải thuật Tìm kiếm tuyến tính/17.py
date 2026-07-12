def tim_linh_canh(a, x):
    n = len(a)
    a.append(x)     
    i = 0
    while a[i] != x:
        i += 1
    a.pop()         
    if i == n:
        return -1
    return i
a = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    p = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(p)
x = int(input("Nhập giá trị cần tìm: "))
ketqua = tim_linh_canh(a,x)
if ketqua !=-1:
    print(f"Tìm thấy {x} ở vị trí {ketqua}")
else:
    print("Không tìm thấy")
# Dùng phương pháp lính canh sẽ giúp giảm gần một nửa số để tính ra kết quả so với phép so sánh