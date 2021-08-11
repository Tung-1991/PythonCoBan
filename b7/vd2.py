file = open('SinhVien.txt','a',encoding='utf-8')
while True:
    maSV = input("msv: ")
    if maSV=="":
        break
    tenSV = input("tenSV: ")
    if tenSV=="":
        break
    lop = input("lop: ")
    if lop=="":
        break
    QueQUan = input("Quequan: ")
    if QueQUan=="":
        break
    file.write("\t".join([maSV,tenSV,lop,QueQUan])+"\n")
file.close()
print("danh sach sinh vien vua nhap")
file = open('SinhVien.txt','r',encoding='utf-8')
for sv in file.readlines():
    print(sv)
file.close()

