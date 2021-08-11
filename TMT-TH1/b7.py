def thang(i):
    switcher = {
        1: '31',
        2: '28',
        3: '31',
        4: '30',
        5: '31',
        6: '30',
        7: '31',
        8: '31',
        9: '30',
        10: '31',
        11: '30',
        12: '31',
    }
    return switcher.get(i, "Invalid day of week")
n = int(input("nhap nam: "))
i = int(input("nhap thang: "))
if n%4==0 and n%100 !=0:
    print(n,"la nam nhuan")
    if i == 2:
        print("so ngay",29)
else:
    print(thang(i))