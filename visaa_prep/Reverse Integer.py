n = int(input().strip())
int_min = -2147483648
int_max = 2147483647
if n<0:
    sign = -1
    n =abs(n)
else:
    sign = 1
r = int(str(n)[::-1])
r *=sign
if r < int_min or r > int_max:
    print(0)
else:
    print(r)
