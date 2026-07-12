import math

A = 0.618

m = 10

arr = [10,20,30,40]

for i in arr:

    hash = math.floor(m * ((i * A) % 1))

    print(i,"->",hash)