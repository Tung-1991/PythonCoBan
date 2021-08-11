n = int(input("xin moi nhap n = "))
x = float(input("xin moi nhap x = "))
s = 0
for i in range(1,n+1):
    s = s+ x**(2*i)
print("tong ",s,)