fashion = []
for i in range(1,11):
    doanhso = int(input("nhap doanh so cua hang"+str(i)+':'))
    fashion.append(doanhso)
print("lst_fashion = ",fashion)
while(True):
    print("nhap 1: hien thi doanh so ban hang cao nhat")
    print("nhap 2: hien thi doanh so trung binh cua 10 cua hang")
    print("nhap 3: hien thi doanh so sap xep tu cao xuong thap")
    print("nhap 0: ket thuc chuong trinh")
    chon = int(input("ban chon cong viec:"))
    if(chon==1):
        doanhsomax=0
        for doanhso in fashion:
             if(doanhso>doanhsomax):
                 doanhsomax=doanhso
        print('doanh so cao nhat',doanhsomax)
    elif(chon==2):
        s = 0
        for doanhso in fashion:
            s = s + doanhso
        doanhsotb = s/10
        print('doanh so trung binh = ',doanhsotb)
    elif(chon==3):
        fashionsort = sorted(fashion, reverse=True)
        print(fashionsort)
    else:
        break;