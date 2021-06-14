n, m = list(map(int, input().split()))

a = list(map(int, input().strip().split()))[:n]

a.sort()
start = a[0]
end = a[n-1]


def BinarySearch(a, start ,end):
    h = (start + end) / 2
    s = 0
    for i in range(n):
        if a[i] > h:
            s += a[i] - h
    if s == m:
        print('height = ', int(h))
        exit(0)
    elif s < m:
        return BinarySearch(a, start, h - 1)
    elif s > m:
        return BinarySearch(a, h + 1, end)


BinarySearch(a, start, end)
