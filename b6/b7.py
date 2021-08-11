def nhaphocsinh():
    sbd = str(input("nhap sbd: "))
    ten = str(input("nhap ten: "))
    toan = int(input("nhap diem toan: "))
    van = int(input("nhap diem van: "))
    while len(sbd.strip()) !=5:
        sbd = str(input("nhap lai sbd: "))
    while len(ten.strip()) > 25 and len(ten.strip())<0:
        ten = str(input("nhap lai ten: "))
    while toan > 10 and toan < 0:
        toan = str(input("nhap lai diem toan: "))
    while van > 10 and van < 0:
        van = str(input("nhap lai diem van: "))
    return {"SBD":sbd,"Ten":ten,"DiemToan":toan,"DiemVan":van}
def nhapdanhsach():
    lisths=[]
    n = int(input("ban muon nhap bao nhieu hoc sinh: "))
    while n<0:
        n = int(input("nhap lai n:"))
    for i in range(1,n+1):
        print("hoc sinh thu",i)
        lisths.append(nhaphocsinh())
    return lisths
def dtb(a,b):
    return (a+b)/2
def hienthi(dshs):
    print("ket qua hoc sinh")
    for i,hs in enumerate(dshs):
        diemtb = dtb(hs['DiemToan'],hs['DiemVan'])
        if diemtb > 10:
            print("hoc sinh co tong diem >10")
            print("stt",i+1,hs['SBD'],hs['Ten'],hs["DiemToan"],hs["DiemVan"],diemtb)
        if(hs['DiemToan']==0 or hs['DiemVan']==0):
            print("hoc sinh ngu")
            print("stt",i+1,hs['SBD'],hs['Ten'],hs["DiemToan"],hs["DiemVan"],diemtb)
lisths=nhapdanhsach()
hienthi(lisths)





