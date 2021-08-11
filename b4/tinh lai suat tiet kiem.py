von = float(input("nhap so von: "))
thang = int(input("nhap so thang: "))
n = float(input("nhap lai xuat: "))
lx = n/100
for i in range(thang):
    von = von+von*lx
print("sau: " ,str(thang/12) +"nam so du trong tai khoan sinh vien la: ",int(von))

