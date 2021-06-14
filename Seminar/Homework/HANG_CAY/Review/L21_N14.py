import sys
import math
input = sys.stdin.readline

def sum_diff(array, i):
    result = []
    for num in array:
        if num > i:
            result.append(num - i)
        else:
            result.append(0)
    return sum(result)

n, m = input().split()
m = int(m)
array = [int(x) for x in input().split()]
max_num = max(array)
for i in range(max_num):
    diff = sum_diff(array, i)
    if diff < m:
        max_num = i - 1
        break
print(max_num)
