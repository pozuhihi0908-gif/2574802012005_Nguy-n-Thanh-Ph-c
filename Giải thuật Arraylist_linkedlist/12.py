arr = [3, 1, 3, 2, 1]

ketqua = []

for i in range(len(arr)):
    trung = False

    for j in range(len(ketqua)):
        if arr[i] == ketqua[j]:
            trung = True
            break

    if trung == False:
        ketqua.append(arr[i])

print(ketqua)