A = {1,2,3,4}
B = {2,3,4,5}

minA = 1000000
minB = 1000000

for i in A:

    h = (i * 7 + 3) % 11

    if h < minA:
        minA = h

for i in B:

    h = (i * 7 + 3) % 11

    if h < minB:
        minB = h

print("MinHash A:",minA)
print("MinHash B:",minB)

if minA == minB:
    print("Hai tập khá giống nhau")
else:
    print("Hai tập khác nhau")