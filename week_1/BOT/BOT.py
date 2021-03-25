n = int(input())
a = list(map(int, input().strip().split()))[:n]
a = [0] + a
for i in range(1, n+1):
    a[i] = a[i-1] + a[i]

index_left, index_right = 0, 1
left_min, right_max = 0, 1
for i in range(1, n+1):
    if a[left_min] > a[i]:
        left_min = i
    if a[index_right] - a[index_left] < a[i] - a[left_min]:
        index_left = left_min
        index_right = i
print(index_left+1, index_right, a[index_right]-a[index_left])
