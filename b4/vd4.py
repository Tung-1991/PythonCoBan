#kiem tra thang thuoc mua nao trong nam
kt = True
while kt:
    thang = int(input("nhap thang: "))
    if (thang <1 or thang >12):
        print("thang ",thang,"ko hop le")
        print("nhap lai")
    else:
        kt= False
if(thang == 1 or thang == 2 or thang == 3):
    print("thang la mua xuan")
elif(thang == 4 or thang == 5 or thang == 6):
    print("thang la mua Ha")
elif(thang == 7 or thang == 8 or thang == 9):
    print("thang la mua Thu")
else:
    print("thang la mua Dong")