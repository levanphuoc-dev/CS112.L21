# RENEWED - ĐỔI MỚI
## 1. Abstraction (Trừu tượng hóa):
+ Cho trước các số nguyên a, k, b, m, n.
+ Tìm giá trị t nguyên nhỏ nhất, thỏa: (a + b) * t - a * t // k - b * t // m >= n
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: duyệt vòng lặp.
+ Đặc điểm nhận dạng: tìm số nhỏ nhất thõa biểu thức bài toán.
## 3. Algorithm designed(Thiết kế thuật toán):
+ Tim số ngày ít nhất để hoàn thành công việc nếu không có ngày nghỉ:
+ temp_day = n//(a+b)
+ Tính số công việc còn lại khi đã thực hiện được temp_day:
+ count = temp_day(a+b) - a(temp_day//k) - b*(temp_day//m)
+ Kiểm tra chừng nào số công việc đã làm vẫn còn bé hơn số công việc đề ra thì tiếp tục tăng số ngày thực hiện lên
+ In kết quả
## 4. Complexity(Độ phức tạp):
+ Mặc dù sử dụng vòng lặp while, nhưng số lần thực hiện phép toán rất ít ( nhỏ hơn 10), nên độ phức tạp của thuật toán này là O(1).
## 5. Jupyter notebook: [RENEWED.ipynb](/RENEWED/Renewed.ipynb) or [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/levanphuoc-dev/CS112.L21/blob/main/week_3/RENEWED/Renewed.ipynb)
