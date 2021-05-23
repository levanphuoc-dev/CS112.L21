import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0
while (a*d-b*c < 0):
    a = a + 1
    b = b + 1
    temp = math.gcd( a , b )
    a = a // temp
    b = b // temp
    count +=1
if(a*d-b*c):
    print(0)
else:
    print(count)
