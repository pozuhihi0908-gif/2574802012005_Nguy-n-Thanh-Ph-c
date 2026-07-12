m = 5

arr = [10,15,20,25,30]

bucket = [0] * m

for i in arr:
    bucket[i % m] = bucket[i % m] + 1

vaCham = 0

for i in bucket:

    if i > 1:
        vaCham = vaCham + (i * (i - 1)) // 2

print("Số va chạm:", vaCham)