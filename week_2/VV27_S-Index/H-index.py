n = int(input())
c = list(map(int,input().split()))
c = sorted(c,reverse=True)
def findHindex(arr):
    h_index = 0
    for i in range(n,0,-1):
        if c[i-1] >= i:
            h_index = i 
            break
    return h_index
print(findHindex(c))
