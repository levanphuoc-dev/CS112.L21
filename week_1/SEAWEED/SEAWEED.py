n,k = map(int,input().split())
def solve(n,k):
    fibo = [0,1]
    sum = 1
    for i in range(0,2*k):
        fibo.append(fibo[1]+fibo[0])
        fibo.pop(0)
        if i % 2 == 0:
            sum+=fibo[1]
    return sum*n%(10**9+7)
print(solve(n,k))
