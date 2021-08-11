a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
ua = 0
ub = 0

for i in range(2, a):
    if a % i == 0:
        ua = i
        print(ua)
print("uoc cua",a,'la',ua)

for j in range(2, b):
    if b % j == 0:
        ub = j
print("uoc cua",b,'la',ub)

if (ua == ub):
    print("uoc chung lon nhat",ua)
else:
    print("khong co uoc lon nhat")

#uoc chugn nho nhat cua 1 so
n=int(input("nhap so a:"))
a=[] #dat a lam 1 list
for i in range(2,n):
    if(n%i==0):
        a.append(i) #them list vao a
a.sort() #sap xep mang a
print(a)
print("uoc la:",a[-1])