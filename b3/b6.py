msv = str(input("nhap msv: "))
hoten = str(input("nhap ho ten: "))
diemrl = int(input("nhap diem rl: "))
if(diemrl >100 and diemrl <0):
    print("nhap sai")
elif (diemrl >= 90):
    print("xuat sac")
elif(diemrl <90 and diemrl >=80):
    print("gioi")
elif(diemrl < 80 and diemrl >= 65):
    print("kha")
elif(diemrl < 65 and diemrl >= 50):
    print("trungbinh")
else:
    print("yeu")