arr1 = [1, 3, 5]
arr2 = [2, 4]

arr = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr.append(arr1[i])
        i = i + 1
    else:
        arr.append(arr2[j])
        j = j + 1

while i < len(arr1):
    arr.append(arr1[i])
    i = i + 1

while j < len(arr2):
    arr.append(arr2[j])
    j = j + 1

print(arr)