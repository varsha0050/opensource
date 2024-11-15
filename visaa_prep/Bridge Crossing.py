x,y,z = map(int,input().split())
N = z-y
t = N//x
if y>=z:
    print(0)
else:
    print(t)
