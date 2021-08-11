a = int(input("nhap a: "))
b = int(input("nhap b: "))
c = int(input("nhap c: "))
if ( a < b and a < c):
    print("so nho nhat la:",a)
elif(b < a and b < c ):
    print("so nho nhat la:",b)
else:
    print("so nho nhat la:",c)