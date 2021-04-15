# KHÓA SỐ
## 1. Abstraction (Trừu tượng hóa):
+ Tìm chuỗi số lớn nhất chia hết cho 3 bằng cách đổi vị trí hoặc xóa ký tự tỏng chuỗi số đã cho trước.
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: Duyệt
+ Đặc điểm nhận dạng: Tính chất của số chia hết cho 3
## 3. Algorithm designed (Thiết kế thuật toán):
+ Chuyển input từ kiểu dữ liệu string sang mảng số nguyên
+ Tính tổng của mảng số nguyên đó.
+ Nếu tổng % 3 = 0:
  - Sắp xếp mảng số nguyên theo thứ tự giảm dần
  - In ra mảng số nguyên
+ Nếu tổng % 3 != 0:
  - Tính arr_0, arr_1, arr_2 lần lượt là mảng của số các số chia 3 dư 0, 1, 2
  - Sắp xếp arr_1, arr_2 theo thứ tự giảm dần
  - Nếu tổng % 3 = 1:
    - Nếu len(arr_1) > 0, xóa 1 phân tử nhỏ nhất của arr_1
    - Ngược lại, xóa 2 phần tử nhỏ nhất của arr_2
  - Nếu tổng % 3 = 2:
    - Nếu len(arr_2) > 0, xóa 1 phần tử nhỏ nhất của arr_2
    - Ngược lại, xóa 2 phần tử nhỏ nhất của arr_1
  - Kết quả thu được là các phần tử trong mảng arr_0, arr_1, arr_2 được sắp xếp theo thứ tự giảm dần
## 4. Complexity (Độ phức tạp):
+ Ta chỉ sử dụng một vòng for nên độ phức tạp là O(n)
