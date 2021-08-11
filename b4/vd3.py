#dem so uoc nguyen cua n nhap tu ban phim
n=int(input("nhap so nguyen n = "))
i = 1
dem = 0
if n<0: m = n*-1
else: m = n
print(m)
while(i<=m):
    if n%i==0: dem=dem+1
    i=i+1
print(n,"co so uoc duong la:",dem)