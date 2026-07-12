arr = [1, 2, 3, 4]

trai = 0
phai = len(arr) - 1

while trai < phai:
    tam = arr[trai]
    arr[trai] = arr[phai]
    arr[phai] = tam

    trai = trai + 1
    phai = phai - 1

print(arr)