D={}
kt = 0
while kt != "k":
    kt = str(input("nhap k de dung: "))
    if kt == "k":
        print("ket thuc")
    else:
        k = str(input("nhap key: "))
        v = int(input("nhap value: "))
        D[k]=v
print("tu dien D: ",D)
print("tong value D",sum(D.values()))
sx = dict(sorted(D.items()))
print("sx tang dan:",sx)
n = list(D.values())
for i in n:
    snt = True
    if i < 2:
        snt = False
    else:
        j=2
        while (j<i-1):
            if i%j==0:
                snt = False
                break
            j=j+1
    if snt==True:
        print(i,"la snt")
    else:
        print(i,"ko la snt")
for i in n:
    bn = f"{i:08b}"
    print(i,'sang nhi phan',bn)