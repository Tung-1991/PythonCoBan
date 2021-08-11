n = int(input("nhap vao so dien:"))
if(n <= 50):
    print("tien dien:",n*2000)
elif(n <= 150 and n > 50):
    l1= (n-50)
    print("tien dien  50kwh 2000:",50*2000)
    print("tien dien 100kwh 2500:",l1*2500)
    print("tien dien tong:",l1*2500+50*2000)
elif(n <= 250 and n > 150):
    l1= (n-50-100)
    print("tien dien  50kwh 2000:",50*2000)
    print("tien dien 100kwh 2500:",100*2500)
    print("tien dien 100kwh 3000:",*3000)
    print("tien dien tong:",50*2000+100*2500+l1*3000)
elif (n <= 400 and n > 250):
    l1 = (n-50-100-100)
    print("tien dien  50kwh 2000:", 50 * 2000)
    print("tien dien 100kwh 2500:", 100 * 2500)
    print("tien dien 100kwh 3000:", 100 * 3000)
    print("tien dien 100kwh 3500:", l1 * 3500)
    print("tien dien tong:", 50 * 2000 + 100 * 2500 + 100 * 3000 + l1 * 3500)
elif (n > 400):
    l1 = (n - 50 - 100 - 100 - 100)
    print("tien dien  50kwh 2000:", 50 * 2000)
    print("tien dien 100kwh 2500:", 100 * 2500)
    print("tien dien 100kwh 3000:", 100 * 3000)
    print("tien dien 100kwh 3500:", 100 * 3500)
    print("tien dien 100kwh 4000:", l1 * 4000)
    print("tien dien tong:", 50 * 2000 + 100 * 2500 + 100 * 3000 + 100 * 3500 + l1 * 4000)
else:
    print("khong phai dong tien dien")