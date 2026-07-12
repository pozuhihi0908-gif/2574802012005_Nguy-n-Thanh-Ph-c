arr = []

arr.append(1)
arr.append(2)
arr.append(3)

index = 1

if index >= 0 and index < len(arr):
    print(arr[index])
else:
    print("Index không hợp lệ")

index = 1

if index >= 0 and index < len(arr):
    arr[index] = 10
else:
    print("Index không hợp lệ")

print(arr)
print(len(arr))