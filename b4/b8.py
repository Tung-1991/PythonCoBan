n = int(input("nhap n: "))
x = float(input("nhap x: "))
s = 0
for i in range(1,n+1):
    s = s + x**(2*i+1)
print(s)