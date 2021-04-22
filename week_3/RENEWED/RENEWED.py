import math
a,k,b,m,n = list(map(int,input().split()))
temp_day = n//(a+b)
count = temp_day*(a+b) - a*(temp_day//k) - b*(temp_day//m)
while(count < n ):
    temp = math.ceil((n - count)/(a+b))
    temp_day += temp
    count = temp_day*(a+b) - a*(temp_day//k) - b*(temp_day//m)
print(temp_day)
