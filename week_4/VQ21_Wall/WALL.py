n = int(input())

if n < 1 or n > 10**5:
    exit(0)

oldWalls = list(map(int, input().split()))[:n]

for i in range(len(oldWalls)):
    if oldWalls[i] < 1 or oldWalls[i] > 10**8:
        exit(0)

m = int(input())
if n < 1 or n > 10**5:
    exit(0)

leftoverWoods = list(map(int, input().split()))[:m]

for i in range(len(leftoverWoods)):
    if leftoverWoods[i] < 1 or leftoverWoods[i] > 10**8:
        exit(0)

def checkHeight(h, oldWalls, leftoverWoods, m, n):
    j = 0
    for i in range(n):
        while (j < m and oldWalls[i] + leftoverWoods[j] < h):
            j += 1
        if oldWalls[i] < h and j == m:
            return False
        if oldWalls[i] < h:
            j += 1
    return True

def getResult(h, oldWalls, leftoverWoods, m, n):
    j = 0
    arr_result = []
    for i in range(n):
        while (j < m and oldWalls[i] + leftoverWoods[j] < h):
            j += 1
        if oldWalls[i] < h and j == m:
            return arr_result
        if oldWalls[i] < h:
            arr_result.append([i + 1, j + 1])
            j += 1
    return arr_result


minHeight, maxHeight = 0, int(2*10**8)

while maxHeight - minHeight > 1:
    avgHeight = minHeight + (maxHeight - minHeight) // 2
    check = checkHeight(avgHeight, oldWalls, leftoverWoods, m, n)
    if check:
        minHeight = avgHeight
    else:
        maxHeight = avgHeight

arr_result = getResult(maxHeight - 1, oldWalls, leftoverWoods, m, n)

print(str(maxHeight - 1), str(len(arr_result)), sep=' ', end='\n')
for pos in range(len(arr_result)):
    print(*arr_result[pos], sep=' ', end='\n')
