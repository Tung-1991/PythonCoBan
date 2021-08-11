#lap 1 de a dung la duong
while True:
    a=float(input('so tien gui: '))
    if a>0: break
#lap 2 de kiem tra b>=a
while True:
    b=float(input('so tien can nhan: '))
    if b>=a:break
#lap 3 de tinh so tien
t=0
while (a<b):
    a=a+a*0.05
    t=t+1
    print(a)
print("so thang can gui la:",t)
