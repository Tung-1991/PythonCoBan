from datetime import datetime
year = datetime.now().year
n = int(input("nhap nam sinh: "))
while n<1900:
    n = int(input("nhap lai nam sinh:"))
tuoi = year - n
print("tuoi:" ,tuoi)