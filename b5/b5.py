n = int(input("ban muon nhap bao nhieu Bang Dia: "))
ListBD = []
for i in range(n):
    Ten = input("nhap Ten: ")
    TL = input("nhap The Loai: ")
    SL = float(input("nhap So luong: "))
    Gia = float(input("nhap gia: "))
    ListBD.append({
        "Ten": Ten,
        "TL": TL,
        "SL": SL,
        "Gia": Gia,
    })
print("danh sach bang dia: ",ListBD)
for bd in ListBD:
    if (min(bd['Gia'] for bd in ListBD) == bd['Gia']):
        print("Ten", bd['Ten'],"Theloai", bd['TL'],"Dia gia nho nhat", min(bd['Gia'] for bd in ListBD))