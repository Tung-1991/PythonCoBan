def chuanhoa(s):
    s1 = s.strip()
    s2 = s1.lower()
    s3 = s2.title()
    s4 = s3.split(' ')
    s5 = ' '.join(s4)
    return print(s5)
s = str(input("nhap xau:"))
chuanhoa(s)