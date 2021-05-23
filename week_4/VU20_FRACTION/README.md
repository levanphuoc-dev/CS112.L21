# FRACTION - PHÂN SỐ
## 1. Abstraction (Trừu tượng hóa):
+ Cho trước 4 số nguyên a,b,c,d
+ Mỗi phép biến đổi tăng a,b lên 1 đơn vị rồi lần lượt chia a,b cho GCD(a,b)
+ tìm số lần thực hiện để a*d - b*c = 0
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: duyệt vòng lặp.
+ Đặc điểm nhận dạng: thực hiện lặp với số lần biết trước.
## 3. Algorithm designed (Thiết kế thuật toán):
+ Nhận xét: Phân số a/b phải bé hơn c/d, thì sau các bước thực hiện mới từ a/b có thể biến đổi thành c/d
+ Đầu tiên: ta kiểm tra a/b có lớn hơn hoặc bằng c/d không. nếu có thì print 0 và kết thúc.
+ Nếu không thì:
+ Tạo biến đếm count = 0
+ Thực hiện phép biến đổi đến chừng nào a/b < c/d
+ Trong mỗi lần biến đổi, ta tăng count lên 1 đơn vị
+ Khi thực hiên xong vòng lặp( a/b >= c/d):
+ Nếu a/b = c/d, thì print count và kết thúc chương trình
+ Ngược lại, print 0 và kết thúc chương trình
## 4. Complexity (Độ phức tạp):
+ Độ phức tạp tốt nhất: O(1): khi a/b >= c/d, vòng lặp while không xảy ra.
+ Độ phức tạp xấu nhất: khi a và b luôn là nguyên tố cùng nhau, với X là số lần lặp thì ta có biểu thức :
(a + X ) / ( b + X ) = c/d <=> ad + dX = bc + cX <=> X = (bc - ad)/(d-c).
-> độ phức tạp là O((bc - ad)/(d-c)).
## 5. Jupyter notebook: [Renewed.ipynb](./Fraction.ipynb) or [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/levanphuoc-dev/CS112.L21/blob/main/week_4/VU20_FRACTION/Fraction.ipynb)
