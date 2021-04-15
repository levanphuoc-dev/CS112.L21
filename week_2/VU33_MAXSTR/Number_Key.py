s = list(input().strip())

def convert_arr(s):
    result_int = []
    for i in s:
        result_int.append(ord(i) - ord('0'))
    return result_int

s = convert_arr(s)
sum_s = sum(s)
def password(s):
    if sum_s % 3 == 0:
        s.sort(reverse=True)
        print(*s, sep="")
    else:
        arr_0 = []
        arr_1 = []
        arr_2 = []
        for i in s:
            if i % 3 == 0:
                arr_0.append(i)
            elif i % 3 == 1:
                arr_1.append(i)
            else:
                arr_2.append(i)
        arr_1.sort(reverse=True)
        arr_2.sort(reverse=True)
        if sum_s % 3 == 1:
            if len(arr_1) > 0:
                arr_1 = arr_1[:-1]
            else:
                arr_2 = arr_2[:-2] 
        else:
            if len(arr_2) > 0:
                arr_2 = arr_2[:-1]
            else:
                arr_1 = arr_1[:-2]
        result = arr_0 + arr_1 + arr_2
        result.sort(reverse=True)
        print(*result, sep="")
        return
password(s)
