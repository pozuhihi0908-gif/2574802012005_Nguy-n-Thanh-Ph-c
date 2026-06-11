def timkiem(a,x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return True
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return False
a = [1, 3, 5, 7, 9]
x = 10
ketqua = timkiem(a, x)
if ketqua != x:
    print(f" {ketqua}, không có trong mảng")
else:
    print(f"{ketqua}, có trong mảng")