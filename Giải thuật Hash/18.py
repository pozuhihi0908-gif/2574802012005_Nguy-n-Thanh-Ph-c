s = "abc"

p = 31
m = 1000000007

hash = 0

for i in s:
    hash = (hash * p + ord(i)) % m

print(hash)