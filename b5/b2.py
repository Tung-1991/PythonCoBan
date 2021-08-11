n = int(input("ban muon nhap bao nhieu sinh vien: "))
l = []
for i in range(n):
    msv = int(input("nhap msv:" ))
    ten = str(input("nhap ten: "))
    lop = int(input("nhap lop: "))
    l.append({
        "MSV":msv,
        "Ten":ten,
        "Lop":lop,
    })
for j in l:
    print(j)