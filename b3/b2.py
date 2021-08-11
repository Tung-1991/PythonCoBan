a = int(input("nhap a:"))
b = int(input("nhap b:"))
print(a,"x+",b,"= 0")
if( a == 0 and b !=0):
    print("phuong trinh vo nghiem")
elif(a == 0 and b ==0 ):
    print("phuong trinh co vo so nghiem")
else:
    print("phuong trinh co 1 nghiem",-b/a)