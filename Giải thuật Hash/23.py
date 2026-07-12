arr = [10,20,30,40,50,60]

m = 5

bucket1 = [0] * m
bucket2 = [0] * m

for i in arr:
    bucket1[i % m] = bucket1[i % m] + 1

for i in arr:
    bucket2[(i * 3) % m] = bucket2[(i * 3) % m] + 1

print(bucket1)
print(bucket2)