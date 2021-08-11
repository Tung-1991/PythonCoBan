def ktcsp(n):
    scp=False
    if n < 2:
        scp=True
    else:
        i=2
        while(i<n+1):
            if i**2==n:
                scp=True
                break
            i=i+1
        if scp == False:
            print(n,"ko la scp")
n = int(input("nhap n: "))
for i in range(1,n+1):
    ktcsp(i)
