s = str(input("nhap chuoi s: "))
n = s.split()
print("chuoi vao list: ",n)
print("sap xep tang dan va bang chu cai: ",sorted(n))
print("tu co ky tu dai nhat: ",max(n))
s=[int(i) for i in n if i.isdigit()]
print("cac so trong list:",s)
print("tong binh phuong: ",sum(s)**2)


