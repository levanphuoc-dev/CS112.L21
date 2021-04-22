# NEWNUM
## 1. Abstraction (Trừu tượng hóa):
+ Cho trước 1 số nguyên n.
+ Xác định số nguyên m lớn nhất, khác n đúng 1 chữ số và chia hết cho 3.
## 2. Pattern recognition (Nhận dạng mẫu):
+ Kỹ thuật áp dụng: Duyệt
+ Đặc điểm nhận dạng: Tính chất của số chia hết cho 3
## 3. Algorithm designed (Thiết kế thuật toán):
+ Chuyển input từ kiểu dữ liệu string sang mảng số nguyên s
+ Tính q =  modulo của sum(s) cho 3
+ đặt flag = True
+ Lần lượt duyệt các phần tử của s từ trái sang phải:
  - Thiết lập 1 biến tạm temp = s[i]%3 + 6 - q (để đưa về số chia hết cho 3)
  -  Nếu temp <7, tăng temp lên 3 đơn vị ( đưa về số lớn nhất )
  -  Nếu temp > s[i], thì gán s[i] = temp, flag = False, in kết quả và kết thúc chương trình
  -  Ngược lại, tiếp tục duyệt
+ Nếu khi duyệt hết s, nhưng flag = True ( tức chưa có phần tử nào được thay)
  - Tạo biến tạm t = s[-1]%3 + 6 - q 
  - Nếu s[-1] = t, s[-1] = t - 3
  - Ngược lại, s[-1] = t, in kết quả và kết thúc chương trình
## 4. Complexity (Độ phức tạp):
+ Ở trường hợp tốt nhất: độ phức tạp là O(1) ( khi duyệt phần tử đầu tiên thì gán luôn và kết thúc chương trình)
+ Ở trường hợp xấu nhất: độ phức tạp là O(n) ( khi phần tử bị thay là phẩn tử cuối cùng của s)
## 5. Jupyter notebook: [Newnum.ipynb](./Newnum.ipynb) or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/levanphuoc-dev/CS112.L21/blob/main/week_3/NEWNUM/Newnum.ipynb#scrollTo=qb4iIpCScm9L)
