def nhaphocsinh():
    while True:
        mhs = input("nhap ma hoc sinh: ")
        if len(mhs.strip())>0:
            break
    while True:
        hoten = input("nhap ho ten: ")
        if len(hoten.strip())>0:
            break
    while True:
        toan = float(input("nhap diem toan"))
        if toan >= 0 and toan <= 10:
            break
    while True:
        viet = float(input("nhap diem van"))
        if viet >= 0 and viet <= 10:
            break
    return {'MHS':mhs,'HoTen':hoten,'Toan':toan,'Viet':viet}
def nhapds():
    lisths=[]
    while True:
        n = int(input("ban muon co bao nhieu hoc sinh"))
        if n >= 0: break;
    for i in range(1,n+1):
        print("hoc sinh thu: ",i)
        lisths.append(nhaphocsinh())
    return lisths
def diemtb(diemtoan,diemtiengviet):
    return (diemtoan+diemtiengviet)/2
def xeploai(dtb):
    xl=''
    if(dtb>=9 and dtb<=10):
        xl="xuat sac"
    elif(dtb>=8 and dtb<9):
        xl="gioi"
    elif (dtb >= 7 and dtb < 8):
        xl = "kha"
    elif(dtb>=5 and dtb<7):
        xl="trung binh"
    else:
        xl="yeu"
    return xl
def hienthi(dshs):
    print("ket qua hoc sinh")
    for i,hs in enumerate(dshs):
        dtb=diemtb(hs['Toan'],hs['Viet'])
        xepl=xeploai(dtb)
        print(i+1,hs['MHS'],hs['HoTen'],hs['Toan'],hs['Viet'],dtb,xepl)
lisths=nhapds()
hienthi(lisths)
