#tinh gia tri cua da thuc
pn = dict();
sm =0
while True:
    while True:
        sm = int(input("nhap so mu hoac -1 de ket thuc: "))
        if(sm >= -1):break;
    if(sm==-1):break;
    hs = float(input(("nhap he so x^",str(sm))))
    if (hs != 0): pn[sm]=hs
strpol=''
for pow in sorted(pn.keys()):
        if(pn[pow]>0):
            strpol = strpol,"+",str(pn[pow]),'*x^',str(pow)
        else:
            strpol = strpol," ",str(pn[pow]),'*x^',str(pow)
print('p =',strpol.strip('+').strip())

x=float(input("nhap gia tri x= "))
val=sum(pn[pow]*x**pow for pow in pn)
print("gia tri cua da thuc",str(x),"la",str(val))