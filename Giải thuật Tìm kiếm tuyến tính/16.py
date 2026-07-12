def ten(a, x):
   vitrigan = 0
   chenhlech = abs(a[0] - x)
   for i in range(1, len(a)):
        if abs(a[i] - x) < chenhlech:
            chenhlech = abs(a[i] - x)
            vitrigan = i
   return a[vitrigan], vitrigan
a = []
n = int(input("Nhập số lượng phần tử của mảng: "))
for i in range(n):
   p = int(input(f"Nhập phần tử thứ {i+1}: "))
   a.append(p)
x = int(input("Nhập giá trị cần tìm: "))
giatri, vitrigannhat = ten(a, x)
print(f"Số {x} có giá trị gần {giatri} và ở vị trí {vitrigannhat}")