a = [1,2,3]
b = [2,3,4]

tap = {}

for i in a:
    tap[i] = 1

for i in b:
    if i in tap:
        print(i,end=" ")