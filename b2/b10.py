email = str(input(("nhap so email: ")))
kt = email.count("@" and ".")
print("KT co @ va .: ",bool(kt))

re = email.replace('@','.')
kte = re.split(".")
listToStr = ' '.join(map(str, kte))
ktspace = listToStr.count(" ")
print(ktspace)
print("co 3 gia tri: ",listToStr)
print("kt xem cac gia tri x y z co rong khong: ",bool(ktspace == 2))


