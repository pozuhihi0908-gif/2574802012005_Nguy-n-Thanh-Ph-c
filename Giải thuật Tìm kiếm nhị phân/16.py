def co_the_an(pile, h, toc_do):
    gio = 0
    for i in range(len(pile)):
        gio += (pile[i] + toc_do - 1) // toc_do
    return gio <= h
def koko_an_chuoi(pile, h):
    left = 1
    right = max(pile)
    ketqua = right
    while left <= right:
        mid = (left + right) // 2
        if co_the_an(pile, h, mid):
            ketqua = mid
            right = mid - 1
        else:
            left = mid + 1
    return ketqua
pile = [3, 6, 7, 11]
h = 8
print(koko_an_chuoi(pile, h))