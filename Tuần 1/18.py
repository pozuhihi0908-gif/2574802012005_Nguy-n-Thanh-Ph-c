def ma_tran(a, x):
   for i in range(len(a)):
      for j in range(len(a[i])):
        if a[i][j] == x:
          return i, j
   return -1, -1
a = []
d = int(input("Nhập số dòng của mảng: "))
c = int(input("Nhấp số cột của mảng: "))
for i in range(d):
   hang = []
   for j in range(c):
     p = int(input(f"Nhập phần tử [{i}][{j}]: "))
     hang.append(p)
   a.append(hang)
x = int(input("Nhập giá trị cần tìm: "))
timdong, timcot = ma_tran(a, x)
if timdong != -1:
   print(f"Phần tử {x} đươc tìm thấy ở dòng {timdong} và ở cột {timcot}")
else:
   print(f"Không tìm thấy dòng và cột của phần từ {x}")  