capacity = 2
arr = [0] * capacity
size = 0

for x in [1, 2, 3, 4, 5]:

    if size == capacity:
        capacity = capacity * 2

        mang_moi = [0] * capacity

        for i in range(size):
            mang_moi[i] = arr[i]

        arr = mang_moi

    arr[size] = x
    size = size + 1

for i in range(size):
    print(arr[i], end=" ")