arr1 = input()
A = input()
arr1 = list(map(int,arr1.split()))
M = arr1[1]
A = list(map(int,A.split()))
x = 0
y = max(A)
h = (x + y) // 2


def calS(a, h):
    s = 0
    for i in A:
        if i > h:
            s += i - h
    return s


k = calS(A, h)
while k != M and y-x > 1:
    if k > M:
        x = h
    elif k < M:
        y = h
    h = (x + y) // 2
    k = calS(A, h)

if k == M:
    print(h)
else:
    print(x)
