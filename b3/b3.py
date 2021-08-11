import math as m
a = int(input("nhap a:"))
b = int(input("nhap b:"))
c = int(input("nhap c:"))
print(a,"x^2+",b,"x+",c,"= 0")
d = b**2-4*a*c
print("delta = ",d)
if(d < 0):
    print("phuong trinh vo nghiem")
elif(d == 0):
    print("phuong trinh co nghiem kep:",-b/2*a)
else:
    print("phuong tinh co 2 nghiem phan biet")
    print("x1= ",((-b+m.sqrt(d))/2*a))
    print("x2= ",((-b-m.sqrt(d))/2*a))
