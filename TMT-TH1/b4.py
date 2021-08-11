a = int(input("nhap a: "))
b = int(input("nhap b: "))
c = int(input("nhap c: "))
a1 = int(input("nhap a1: "))
b1 = int(input("nhap a2: "))
c1 = int(input("nhap a3: "))

print("he pt 1: ",a,"X +",b,"Y =",c)
print("he pt 2: ",a1,"X +",b1,"Y =",c1)
x=0
y=0
if a == 0:
    y = c/b
else:
    y = (a*c1-a1*c)/(a*b1-b*a1)
    x = (c-b*y)/a
print('X',x)
print('Y',y)