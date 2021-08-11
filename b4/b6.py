n = int(input("Nhập số nguyên dương n = "));
print("so vua nhap co",len(str(n)),"chu so")
s = 0;
while (n > 0):
    s = s + n % 10; #chia lay phan du vd 123 lay 3
    n = int(n / 10);  #chia tiep so vd 123 thi con 12
print("Tổng các chữ số là", s);


#c2 tu so chuyen sang list rồi cộng vòa
num = 1234
lst = [int(i) for i in str(num)]
print(lst)
print(sum(lst))

#c3 giống 2
a = 123456
b = str(a)
c = []
for digit in b:
    c.append (int(digit))
print(c)
