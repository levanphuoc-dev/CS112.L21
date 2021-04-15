# H_Index
## 1. Abstraction(Trừu tượng hóa):
+ Tìm số k lớn nhất sao cho mảng n có k số có giá trị lơn hơn hoặc bằng k.
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: Vét cạn (duyệt mảng).
+ Đặc điểm nhận dạng:
  - Ví dụ cho mảng input theo đề bài là: '[8, 5, 3, 4, 10]'
    + Với k = 1 có 5 phần tử >= 1 (Không thỏa)
    + Với k = 2 có 5 phần tử >= 2 (Không thỏa)
    + Với k = 3 có 5 phần tử >= 3 (Không thỏa)
    + Với k = 4 có 4 phần tử >= 4 (Thỏa)
    + Với k = 5 có 3 phần tử >= 4 (Không thỏa)
  - Với k = 4 thỏa điều kiện đề bài
## 3. Algorithm designed (Thiết kế thuật toán):
+ Sắp xếp mảng nhập vào theo thứ tự giảm dần: c = sorted(c,reverse=True)
+ Gán h_index = 0
+ Duyệt mảng:
  - Nếu c[i-1] >= i thì h_index = i rồi dừng vòng lặp
+ Kết quả bài toán là giá trị h_index thu được.
## 4. Complexity (Độ phức tạp):
+ Chương trình chỉ sử dụng một vòng lặp nên độ phức tạp là O(n)


