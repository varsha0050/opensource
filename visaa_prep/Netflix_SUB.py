a,b,c,x = map(int,input().split())
if a+b>=x or b+c>=x or c+a>=x:
    print("YES")
else:
    print("NO")
