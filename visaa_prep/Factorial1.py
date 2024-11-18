def cal_fact(n):
    f = 1
    for i in range(1,n+1):
        f *=i
    return f
n = int(input().strip())
print(cal_fact(n))
