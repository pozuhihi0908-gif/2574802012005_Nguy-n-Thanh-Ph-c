def ten(a, x):
   for i in range(len(a)):
      if a[i].lower() == x.lower():
         return i
   return -1
a = []
n = int(input("Nhập số lượng tên của mảng: "))
for i in range(n):
   p = input(f"Nhập tên: ")
   a.append(p)
x = input("Nhập tên cần tìm: ")
ketqua = ten(a, x)
if ketqua != -1:
   print(f"Tên {x} đươc tìm thấy ở vị trí thứ {ketqua}")
else:
   print(f"Không tìm thấy tên {x} trong mảng")  