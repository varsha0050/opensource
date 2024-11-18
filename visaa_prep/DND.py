n,m = map(int,input().split())
arr = list(map(int,input().split()))
n1 = 0
n2 = 0
for num in arr:
    if num % m == 0:
        n2 += num
    else:
        n1 += num
print(n2 - n1)
