a = int(input("nhap a: "))
b = int(input("nhap b: "))
ch = input("nhap toan tu +,-,*,/: ")
if (ch == '+' ):
    print(a+b)
elif(ch == "-"):
    print(a-b)
elif (ch == "*"):
    print(a * b)
elif (ch == "/"):
    print(a / b)
else:
    print("ch ko phai toan tu")