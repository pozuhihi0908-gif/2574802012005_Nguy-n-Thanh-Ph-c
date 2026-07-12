1.
-Tìm kiếm tuyến tính là duyệt từng phần tử có trong mảng và so sánh với giá trị x đã cho, trong quá trình duyệt nếu tìm thấy phần tử cần tìm ở vị trí nào thì sẽ dừng ở vị trí đó và xuất ra vị trí phần tử đang đứng. Ngược lại nếu đã duyệt hết tất cả phần tử ở trong phần tử thì sẽ hiện không tìm thấy
-Input: nhập số cần tìm, sau khi nhập nó sẽ tìm kiếm và duyệt từng phần tử
-Output: 
+Trường hợp 1: nếu đã tìm thấy phần tử ở vị trí bất kì nào đó sẽ xuất ra vị trí đã tìm thấy phần tử
+Trường hợp 2: nếu đã duyệt hết tất cả phần tử có trong mảng nhưng vẫn không tìm thấy thì sẽ xuất ra không tìm thấy
2.
B1. A[0] = 7 != 5 = x
B2. i = 0 + 1 = 1

B1. A[1] = 3 != 5 = x
B2. i = 1 + 1 = 2

B1. A[2] = 9 != 5 = x
B2. i = 2 + 1 = 3

B1. A[3] = 12 != 5 = x
B2. i = 3 + 1 = 4

B1. A[4] = 5 = x -> Đã tìm thấy phần tử cần tìm ở vị trí i = 5. Dừng kết thúc
3.
(a) = 7 đếm 1 lần
(b) = 1 đếm 7 lần
(c) = 100 đếm hết và không tìm thấy
Với mỗi vị trí sẽ thực hiện 1 lần so sánh, nếu so sánh đến cuối vẫn không tìm thấy thì sẽ dừng so sánh và cho kết quả không tìm thấy
4.
(a) số phép so sánh là 1
(b) số phép so sánh là hết mảng 
(c) số phép so sánh từ ở giữa mảng đến hết mảng
5.
Không. Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước. Vì thuật toán hoạt động bằng cách duyệt lần lượt từng phần tử từ đầu đến cuối và so sánh với giá trị cần tìm. Dù dữ liệu có sắp xếp hay không, thuật toán vẫn tìm được kết quả.
So sánh ngắn gọn với tìm kiếm nhị phân:
Tiêu chí	                    Tìm kiếm tuyến tính	                            Tìm kiếm nhị phân
Điều kiện áp dụng	            Không cần mảng sắp xếp	                        Bắt buộc mảng đã sắp xếp
Cách tìm	                    Duyệt từng phần tử	                            Chia đôi phạm vi tìm kiếm
Độ phức tạp tốt nhất	        O(1)	                                        O(1)
Độ phức tạp trung bình	        O(n)	                                        O(log n)
Độ phức tạp xấu nhất	        O(n)	                                        O(log n)