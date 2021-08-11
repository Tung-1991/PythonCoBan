def tong(n):
    s=0
    for i in range(n):
        s = s + 1/(2*i+1)
        print(i)
    return s
n = int(input("nhap n: "))
print(tong(n))