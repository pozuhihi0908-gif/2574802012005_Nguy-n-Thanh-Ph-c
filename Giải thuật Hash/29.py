m = 10

bit = [0] * m

arr = [12,25,37]

for i in arr:

    h1 = i % m
    h2 = (i * 3) % m

    bit[h1] = 1
    bit[h2] = 1

print(bit)

x = 25

h1 = x % m
h2 = (x * 3) % m

if bit[h1] == 1 and bit[h2] == 1:
    print("Có thể tồn tại")
else:
    print("Chắc chắn không có")