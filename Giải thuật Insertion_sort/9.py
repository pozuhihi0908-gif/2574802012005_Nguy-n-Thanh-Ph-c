a = [5, 2, 4, 6, 1, 3]

n = len(a)

compare = 0

for i in range(1, n):

    key = a[i]

    left = 0
    right = i - 1

    while left <= right:

        compare += 1

        mid = (left + right) // 2

        if key < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    j = i - 1

    while j >= left:
        a[j + 1] = a[j]
        j -= 1

    a[left] = key

print(a)
print("So lan so sanh:", compare)