def tuyentinh(array, n, x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1
array = [15,25,80,30,60,50,110,100,130,180]
x = 185
n = len(array)
result = tuyentinh(array, n, x)
print(f"Phần tử tìm thấy được tại vị trí {result}")