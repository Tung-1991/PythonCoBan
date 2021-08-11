L = []
kt = True
print("n = 0  de ket thuc")
while kt:
    n = int(input("nhap n: "))
    L.append(n)
    if (n==0):
        kt=False
print(L)
print("gia tri lon nhat",max(L))
print("tong cac phan tu",sum(L))
print("sap xep tang dan",sorted((L)))
for i in L:
    if (i>0):
        print(i)
for j in L:
    if (j<0):
        print(j)