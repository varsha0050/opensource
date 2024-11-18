n = int(input().strip())
if 1<=n<=12:
    if 3<=n<=5:
        print("Spring")
    elif 6<=n<=8:
        print("Summer")
    elif 9<=n<=11:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
