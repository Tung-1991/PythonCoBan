import nltk
def tach(x):
    d = x.read()
    tokens = nltk.word_tokenize(d)
    #print(type(tokens))
    print("do dai: ",len(tokens))
    print(tokens[0:10])
    return tokens

AG = open('An Giang.txt','r',encoding='utf-8')
BN = open('Bac Ninh.txt','r',encoding='utf-8')
BT = open('Binh Thuan.txt','r',encoding='utf-8')
CB = open('Cao Bang.txt','r',encoding='utf-8')
HN = open('Ha Noi.txt','r',encoding='utf-8')
HP = open('Hai Phong.txt','r',encoding='utf-8')
LS = open('Lang Son.txt','r',encoding='utf-8')
LC = open('Lai Chau.txt','r',encoding='utf-8')
TN = open('Thai Nguyen.txt','r',encoding='utf-8')
HCM = open('TP HCM.txt','r',encoding='utf-8')
lAG = tach(AG)
lBN = tach(BN)
lBT = tach(BT)
lCB = tach(CB)
lHN = tach(HN)
lHP = tach(HP)
lLS = tach(LS)
lLC = tach(LC)
lTN = tach(TN)
lHCM = tach(HCM)

tudien = {}
for j in lAG:
        tudien[j]=1
for j in lBN:
        tudien[j] = 2
for i in lBT:
        tudien[i] = 3
for j in lCB:
        tudien[j] = 4
for i in lHN:
        tudien[i] = 5
for j in lHP:
        tudien[j] = 6
for i in lLS:
        tudien[i] = 7
for j in lLC:
        tudien[j] = 8
for i in lTN:
        tudien[j] = 9
for j in lHCM:
        tudien[j] = 10
sorted(tudien.values())
print(tudien)
n = input("nhập từ truy vấn: ")
for i in tudien:
    if n == i:
        print(i, ":", tudien[i])
m = int(input("nhập stt: "))
if m == 1:
    print(lAG)
elif m ==2:
    print(lBT)
elif m ==3:
    print(lCB)
elif m ==4:
    print(lBN)
elif m ==5:
    print(lHN)
elif m ==6:
    print(lHP)
elif m ==7:
    print(lLC)
elif m ==8:
    print(lLS)
elif m ==9:
    print(lTN)
elif m ==10:
    print(lHCM)
else:
    print("ko co STT nay")