x = float(input("nhap x: "))
y = float(input("nhap y: "))
z = 0
if x**2 <= 1 and y**2 <=1:
    z = x**2+y**2
    print(z)
elif x**2 >1 and y**2 >1 and x>=y:
    z = x + y
    print(z)
elif x**2 >1 and y**2 >1 and x<y:
    z = x ** 3 + y ** 3
    print(z)
