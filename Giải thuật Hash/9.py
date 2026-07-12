arr = [2,7,11,15]

target = 9

bang = {}

for i in range(len(arr)):

    can = target - arr[i]

    if can in bang:
        print(bang[can], i)
        break

    bang[arr[i]] = i