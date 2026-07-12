def linear_search(a, x):
   for i in range(len(a)):
      if a[i] == x:
         return i
   return -1
a = []
x = int(input("Nhập giá trị cần tìm: "))
n = int(input("Nhập số phần tử của mảng: "))
for i in range(n):
   p = int(input(f"Nhập phần tử thứ {i+1}: "))
   a.append(p)
ketqua = linear_search(a, x)
if ketqua != -1:
   print(f"Phần tử {x} đươc tìm thấy ở vị trí thứ{ketqua}")
else:
   print(f"Không tìm thấy vị trí của phần từ {x}")  