s = input(str("nhap vao ten"))
#dung de xoa dau cach o dau va cuoi
s1 = s.strip()
print(s1)
#dung de chuyen tat ca ve chu thuong
s2 = s1.lower()
print(s2)
#dung de chu hoa tat ca chu dau
s3 = s2.title()
print(s3)
#dung de tach tat ca ky tu boi dau cach
s4= s3.split()
print(s4)
#dung dau cach de ket hop tat ca cac tu lai voi nhau
s5 = " ".join(s4)
print(s5)