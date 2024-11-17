x,y,z = map(int,input().split())
t = x*y
if t <= z*24*60:
    print("YES")
else:
    print("NO")
