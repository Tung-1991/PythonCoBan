def nhaptach():
    a = str(input("nhap ten a: "))
    b = str(input("nhap ten b: "))
    a1 = a.lower().split(" ")
    b1 = b.lower().split(" ")
    print(a1)
    print(b1)
    return a1,b1
def kt(a1,b1):
    for i in a1:
        for j in b1:
            if i == j:
                print("tu",i,"nam trong van ban")

a,b = nhaptach()
kt(a,b)







