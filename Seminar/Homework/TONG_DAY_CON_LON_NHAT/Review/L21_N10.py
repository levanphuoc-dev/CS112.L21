arr = input()
arr = arr[1:len(arr)-1]
arr = list(map(int,arr.split(",")))
k = int(input())
if k in arr or sum(arr) == k:
    print(0)
else:
    arr.sort(reverse=True)
    _min1 = abs(arr[0] - k)
    for i in range(0, len(arr)-1):
        _tem1 = abs(arr[i]-k)
        _min1 = min(_min1,_tem1)
    tem1 = arr[0]
    for i in range(1, len(arr)-1):
        tem1 += arr[i]
        _min1 = min(_min1,abs(tem1-k))

    arr.sort()
    _min2 = abs(arr[0] - k)
    for i in range(0, len(arr)-1):
        _tem2 = abs(arr[i]-k)
        _min2 = min(_min2,_tem2)
    tem2 = arr[0]
    for i in range(1, len(arr)-1):
        tem2 += arr[i]
        _min2 = min(_min2,abs(tem2-k))

    print(min(_min1,_min2))
