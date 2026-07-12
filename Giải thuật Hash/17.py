m = 10

s = "abc"

tong = 0

for i in s:
    tong = tong + ord(i)

print(tong % m)

s = "cba"

tong = 0

for i in s:
    tong = tong + ord(i)

print(tong % m)