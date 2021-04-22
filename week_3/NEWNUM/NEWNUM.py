s = list(input().strip())

def convert_arr(s):
    result_int = []
    for i in s:
        result_int.append(ord(i) - ord('0'))
    return result_int
flag = True
s = convert_arr(s)
modulo_s = sum(s)%3
for i, val in enumerate(s):
    temp = val%3 + 6 - modulo_s
    if(temp<7):
        temp +=3
    if(temp <= val):
        continue
    else:
        s[i] = temp
        flag = False
        break
if(flag):
    t = s[-1]%3 + 6 - modulo_s
    if(s[-1]== t ):
        s[-1] -= 3
    else:
        s[-1] = t
print(*s,sep ='')
