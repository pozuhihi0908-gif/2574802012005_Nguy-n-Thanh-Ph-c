a = 5
b = 7
p = 101
m = 10

arr = [10,20,30,40]

for i in arr:

    hash = ((a * i + b) % p) % m

    print(i,"->",hash)