#cach 1
s = str(input("nhap ten nguoi dung:"))
s1 = s.strip(" ").split(" ")
print("s",s1,)
for i in s1:
    print(i,':',len(i))

#cach 2
ds = input("nhap: ").lower().split(" ")
D = {}
for i in ds:
    if i in ds:
        D[i] = D[i]+1
    else:
        D[i] = 1
print(D)
