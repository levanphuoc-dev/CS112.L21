import math
def addifpositive(sum, term):
    if term>=0:
        sum+=term
a, b= map(int, input().split())
k=list(map(int, input().split()))
woodmin=9999999
index=0
for i in range (max(k)):
    wood=0
    for j in k:
        if j-i>0:
            wood+=j-i
    if wood-b<woodmin and wood-b>=0:
        index=i
print(index)
