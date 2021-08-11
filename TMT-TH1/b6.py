n = float(input("nhap vao so KM:"))
if(n <= 2):
    print("tien:",n*15000)
elif(n <= 5 and n > 2):
    l1= (n-2)
    print("tien 2km 15000:",2*15000)
    print("tien 2km-5km:",l1*13500)
    print("tien tong1:",l1*13500+2*15000)
elif(n > 5 and n <= 120):
    l1 = n-5
    print("tien tong2:",l1*11000+2*15000+3*13500)
elif (n > 120):
    l1 = n-5
    tong = (l1*11000+2*15000+3*13500)*0.9
    print("tien tong3:",tong)
else:
    print("khong phai dong tien dien")