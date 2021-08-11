def gt(n):
    gt=1;
    for i in range(1,n+1):
        gt = gt * i;
    return gt;
while True:
    n = int(input("nhap n:"))
    k = int(input("nhap k:"))
    if(n>=k) and (k>0):
        break;
gtn=gt(n)
gtk=gt(k)
gtnk=gt(n-k)
cnk=gtn/(gtk*gtnk)
print(cnk)