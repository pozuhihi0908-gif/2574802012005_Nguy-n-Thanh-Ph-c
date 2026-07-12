def them_lien_he(ds):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    lh = {
        "ten": ten,
        "sdt": sdt
    }
    ds.append(lh)
    print("Đã thêm liên hệ")
def tim_sdt(ds, ten):
    for lh in ds:
        if lh["ten"].lower() == ten.lower():
            return lh["sdt"]
    return None
def tim_ten(ds, sdt):
    for lh in ds:
        if lh["sdt"] == sdt:
            return lh["ten"]
    return None
def dem_dau_so(ds, dauso):
    dem = 0
    for lh in ds:
        if lh["sdt"].startswith(dauso):
            dem += 1
    return dem
danhsach = []
while True:
    print("\n===== MENU =====")
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số điện thoại theo đầu số")
    print("0. Thoát")
    chon = input("Nhập lựa chọn: ")
    if chon == "1":
        them_lien_he(danhsach)
    elif chon == "2":
        ten = input("Nhập tên cần tìm: ")
        ketqua = tim_sdt(danhsach,ten)
        if ketqua:
            print("Số điện thoại:",ketqua)
        else:
            print("Không tìm thấy")
    elif chon == "3":
        sdt = input("Nhập số điện thoại: ")
        ketqua = tim_ten(danhsach,sdt)
        if ketqua:
            print("Tên:",ketqua)
        else:
            print("Không tìm thấy")
    elif chon == "4":
        dauso = input("Nhập đầu số: ")
        ketqua = dem_dau_so(danhsach,dauso)
        print("Có",ketqua,"liên hệ")
    elif chon == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")