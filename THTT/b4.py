a = input("nhap ds1 : ")
b = input("nhap ds2 : ")
ds1 = a.strip().split()
ds2 = b.strip().split()
ds1.sort()
ds2.sort()
print("ds 1 sau khi sap xep",ds1)
print("ds 2 sau khi sap xep",ds2)
for i in ds1:
    for j in ds2:
        if i == j:
            print("so", i, "giao giua ds1 va ds2")

ds3 = [k for k in ds1 if k not in ds2]
ds4 = [k for k in ds2 if k not in ds1]
print("so co trong ds1 nhung ko co trong ds2",ds3)
print("so co trong ds2 nhung ko co trong ds1",ds4)

if len(ds1) > len(ds2):
    print("hop giua ds1 va ds2",ds1 + ds4)
elif len(ds1) < len(ds2):
    print("hop giua ds1 va ds2", ds2 + ds3)
else:
    print("hop giua ds1 va ds2", ds1 + ds4)

    print("hop giua ds1 va ds2", ds2 + ds3)
