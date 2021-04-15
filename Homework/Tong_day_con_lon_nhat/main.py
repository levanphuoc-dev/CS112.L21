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
  
