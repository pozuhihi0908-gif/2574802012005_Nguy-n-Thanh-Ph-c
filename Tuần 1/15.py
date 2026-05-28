def kiem_tra(b):
   if b < 2:
      return False
   for i in range(2, n+1):
      if b % i == 0:
        return False
   return True
def so_nguyen_to(a):
   for i in range(len(a)):
         if kiem_tra(a[i]):
           return i
   return -1
a = []
n = int(input("Nhập số phần tử của mảng: "))
for i in range(n):
   p = int(input(f"Nhập phần tử thứ {i+1}: "))
   a.append(p)
ketqua = so_nguyen_to(a)
if ketqua != -1:
   print(f"Số nguyên tố đầu tiên là {a[ketqua]} đươc tìm thấy ở vị trí thứ {ketqua}")
else:
   print(f"Không tìm thấy số nguyên tố trong mảng")  