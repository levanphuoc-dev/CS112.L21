# WALL - SỬA HÀNG RÀO
## 1. Abstraction (Trừu tượng hóa):
+ Dùng m tấm gỗ thừa gia cố hàng rào
+ Hàng rào được ghép từ n tấm gỗ
+ Xác định độ cao lớn nhất có thể đạt được của hàng rào sau khi gia cố. Độ cao của hàng rào được tính bằng độ cao tấm gỗ thấp nhất trên hàng rào.
+ Với mỗi h (chiều cao hàng rào sau khi gia cố), ta lưu vị trí (i, j) tìm được (i là vị trí tấm ván ở hàng rào cũ, j là vị trí tấm ván vừa gia cố).
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: Duyệt mảng.
+ Đặc điểm nhận dạng:
  - Tìm chiều cao h với giả thiết của bài toán.
  - Theo giả thiết bài toán, chiều cao h giao động trong khoảng từ 0 đến trường hợp xấu nhất là 2*10**8

## 3. Algorithm designed (Thiết kế thuật toán):
