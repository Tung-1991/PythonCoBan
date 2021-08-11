n = int(input("ban muon nhap bao nhieu mat hang: "))
ListHH = []
for i in range(n):
    Ten = input("nhap Ten: ")
    Soluong = int(input("nhap Soluong: "))
    gia = input("nhap gia: ")
    ListHH.append({
        "Ten": Ten,
        "Soluong": Soluong,
        "gia": gia,
    })
#tinh tong so luong hang hoa
print("danh sach: ",ListHH)
sl = 0
for hh in ListHH:
    print("thong tin hang",hh)
    sl = sl + hh['Soluong']
print("Tong luong hang co trong cua hang:",sl)

print("cac mat hang co soluong nho hon 10:")
for hh in ListHH:
    if hh['Soluong']<10:
        print(hh)

print("cac mat hang co soluong lon hon 50:")
for hh in ListHH:
    if hh['Soluong']>10:
        print(hh)