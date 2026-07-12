def tim_sinh_vien(ds, masv):
    for sv in ds:
        if sv["masv"] == masv:
            return sv
    return None
ds=[]
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    sv={}
    sv["masv"] = input("Nhập mã SV: ")
    sv["hoten"] = input("Nhập họ tên: ")
    sv["dtb"] = float(input("Nhập điểm trung bình: "))
    ds.append(sv)
x = input("Nhập mã sinh viên cần tìm: ")
ketqua = tim_sinh_vien(ds,x)
if ketqua != None:
    print("Thông tin sinh viên:")
    print("Mã SV:",ketqua["masv"])
    print("Họ tên:",ketqua["hoten"])
    print("Điểm TB:",ketqua["dtb"])
else:
    print("Không tìm thấy sinh viên")