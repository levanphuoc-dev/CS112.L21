# SEAWEED - TẢO BIỂN
## 1. Abstraction(Trừu tượng hóa):
  + Tính kết quả n * Fibonacci(2k + 1)
## 2. Pattern recognition(Nhận dạng mẫu):
  + Kỹ thuật áp dụng: Duyệt mảng
  + Đặc điểm nhận dạng:
  Với số cá thể bàn đâu n = 1, theo yêu cầu đề bài ta có:
    + Ngày 0: 1 cá thể sinh ra
    + Ngày 1: 3 cá thể sinh ra
    + Ngày 2: 5 cá thể sinh ra
    + Ngày 3: 13 cá thể sinh ra
    + Ngày 4: 34 cá thể sinh ra
    + Ngày 5: 89 cá thể sinh ra
  Từ suy luận trên ta rút ra được công thức của n cá thể sau k ngày là n * Fibonacci(2k + 1)
 ## 3. Algorithm designed(Thiết kế thuật toán):
    + Gán fibo = [0,1], sum = 1
    + Duyệt mảng chạy từ 0 đến 2k:
      - Thêm fibo[1]+fibo[0] vào list fibo vừa khởi tạo trên
      - Xóa số 0 ra khỏi list fibo
      - Nếu i % 2 == 0 thì
        - Cộng fibo[1] vào sum
    + Trả về sum*n%(10**9+7)
 ## 4. Complexity(Độ phức tạp):
  + Đối với bài toán này ta sử dụng một vòng for nên độ phức tạp là O(n)
  
