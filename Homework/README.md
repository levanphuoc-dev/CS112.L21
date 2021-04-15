## TỔNG DÃY CON NHỎ NHẤT
## 1. Abstraction(Trừu tượng hóa):
  + Tính hiệu nhỏ nhất của tổng các phần tử của substring từ string ban đầu với biến target đề bài cho.   
## 2. Pattern recognition(Nhận dạng mẫu):
  + Kĩ thuật được áp dụng: chia để trị,bitmask.
  + Đặc điểm nhận dạng: bài toán ban đầu có thể chia thành các bài toán con không gối nhau có cách xử lí tương tự
## 3. Algorithm designed(Thiết kế thuật toán):
  + Divide: chia mảng ban đầu thành 2 mảng con
  + Conquer: Tính tổng các phần tử substring  từ string ban đầu
  + Combine: kết hợp kết quả của 2 mảng con, tìm ra kết quả phù hợp bằng chạy vòng lặp
## 4. Code tham khảo(các bạn có cách chia khác, hay cách hay hơn thì góp ý với chúng mình để mọi người cùng tham khảo):
def helper(arr): #conquer
    n = len(arr)
    ans = {0}
    # sử dụng bitmask để tính sum cho từng substring
    for mask in range(1, 1 << n):
        ss = 0
        for i, val in enumerate(arr):
            if (1 << i) & mask:
                    ss += val
        ans.add(ss)
    return list(ans)
def minAbsDifference(nums, target):
    n = len(nums)
    n_2 = n // 2
    s1, s2 = helper(nums[:n_2]), helper(nums[n_2 :]) #divide
    s1.sort()
    s2.sort()
    ans = abs(target)
    i1, i2 = 0, len(s2) - 1
    while i1 < len(s1) and i2 >= 0: #combine
        cur = s1[i1] + s2[i2]
        ans = min(ans, abs(cur - target))
        if cur == target:
            return 0
        elif cur > target:
            i2 -= 1
        else:
            i1 += 1
    return ans
  
 
 ## 4. Complexity(Độ phức tạp):
   + O(n * 2 ^ (n // 2)
