print("hello world")

# đây là khối lệnh kiểm tra năm nhuận
# nếu year chia hết cho 4 mà không chia hết cho 100 hoặc chia hết cho 400 thì year là năm nhuận

year=2011
if (year % 4==0 and year %100 !=0) or (year % 400 ==0):
    print("Nam: ",year, "la nam nhuan")
else:
    print("Nam: ",year, "khong la nam nhuan")

# giai chuong trinh ax+b=0
# he so a = 0 va b = 0 thi vo nghiem
# he so a = 0 va b != 0 thi vo so nghiem
# he so a !=0 va b !=0 thi co nghiem x=-b/a

a=0
b=113
if(a==0 and b==0):
    print("phuong trinh vo so nghiem")
elif (a==0 and b !=0):
    print("phuong trinh co vo so nghiem")
else:
    print( "phuong trinh khong co x=", -b/a)