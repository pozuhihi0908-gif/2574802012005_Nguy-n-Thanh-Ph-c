arr = [[8,10],[1,3],[2,6],[15,18]]

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i][0] > arr[j][0]:
            tam = arr[i]
            arr[i] = arr[j]
            arr[j] = tam

ketqua = []

batdau = arr[0][0]
ketthuc = arr[0][1]

for i in range(1,len(arr)):

    if arr[i][0] <= ketthuc:

        if arr[i][1] > ketthuc:
            ketthuc = arr[i][1]

    else:
        ketqua.append([batdau,ketthuc])
        batdau = arr[i][0]
        ketthuc = arr[i][1]

ketqua.append([batdau,ketthuc])

print(ketqua)