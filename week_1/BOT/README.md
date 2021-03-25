# BOT - TRAM THU PHÍ
## 1. Abstraction(Trừu tượng hóa):
  + Tìm p, q và mảng con lớn nhất nằm trong khoảng p đến q sao cho lãi nhiều nhất hoặc lỗ ít nhất. Nếu có nhiều cách chọn thì chọn p nhỏ nhất.
## 2. Pattern recognition(Nhận dạng mẫu):
  + Kĩ thuật được áp dụng: Duyệt mảng, gắn biến tạm.
  + Đặc điểm nhận dạng: Chọn khoảng từ p đến q sao cho lợi nhuận cao nhất hoặc lỗ ít nhất.
## 3. Algorithm designed(Thiết kế thuật toán):
  + Thiết lập lại chỉ số của mảng sao cho chạy từ 1 -> n
  + Gán chỉ số đại diện cho q, p lần lượt là index_left, index_right = 0, 1
  + Duyệt mảng:
    - Nếu a[left_min] > a[i] thì:
       - left_min = i
    - Nếu a[index_right] - a[index_left] < a[i] - a[left_min] thì
       - index_left = left_min
       - index_right = i
  + In ra kết quả
 
 ## 4. Complexity(Độ phức tạp):
   + Ta chỉ chạy 2 vòng lặp liên tiếp cho chương trình nên độ phức tạp là O(n)
