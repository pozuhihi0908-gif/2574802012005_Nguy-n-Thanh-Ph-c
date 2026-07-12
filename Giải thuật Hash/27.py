arr = [1,2,3]

hash = 0

for i in arr:
    hash = hash ^ i

print(hash)

arr = [3,1,2]

hash = 0

for i in arr:
    hash = hash ^ i

print(hash)