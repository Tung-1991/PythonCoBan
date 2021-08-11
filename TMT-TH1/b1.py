import math as m
xa = int(input("nhap xa:"))
ya = int(input("nhap ya:"))
A = lsta=[]
A.append(xa)
A.append(ya)
print("toa do A:",A)
xb = int(input("nhap xb:"))
yb = int(input("nhap yb:"))
B = lstb=[]
B.append(xb)
B.append(yb)
print("toa do B:",B)
xc = int(input("nhap xc:"))
yc = int(input("nhap yc:"))
C = lstc=[]
C.append(xc)
C.append(yc)
print("toa do C:",C)
AB=m.sqrt((xb-xa)**2+(yb-ya)**2)
AC=m.sqrt((xc-xa)**2+(yc-ya)**2)
BC=m.sqrt((xc-xb)**2+(yc-yb)**2)
print("khoảng cách AB",AB)
print("khoảng cách AC",AC)
print("khoảng cách BC",BC)

if (AB==AC and AC==BC and AB==BC):
    print("la tam giac deu")

if (AB==AC or AC==BC or AB==BC):
    print("la tam giac can")

if (AB**2==AC**2+BC**2 or AC**2==AB**2+BC**2 or BC**2==AC**2+AB**2):
    print("la tam giac vuong")

if ((AB**2==AC**2+BC**2 or AC**2==AB**2+BC**2 or BC**2==AC**2+AB**2) and (AB==AC or AC==BC or AB==BC)):
    print("la tam giac vuong can")