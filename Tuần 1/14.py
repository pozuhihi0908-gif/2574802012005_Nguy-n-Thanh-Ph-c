def so_chan(a):
   for i in range(len(a)):
         if a[i] % 2 == 0:
           return i
   return -1
a = []
n = int(input("Nhập số phần tử của mảng: "))
for i in range(n):
   p = int(input(f"Nhập phần tử thứ {i+1}: "))
   a.append(p)
ketqua = so_chan(a)
if ketqua != -1:
   print(f"Số chẵn đầu tiên là {a[ketqua]} đươc tìm thấy ở vị trí thứ {ketqua}")
else:
   print(f"Không tìm thấy số chẵn trong mảng")  