n,x,y = map(int,input().split())
max_m = n*x
if y<=max_m and y%x==0:
    print("YES")
else:
    print("NO")
