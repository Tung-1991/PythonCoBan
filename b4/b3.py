import time
hh = int(input("nhap gio: "))
mm = int(input("nhap phut: "))
ss = int(input("nhap giay: "))
k = int(input("nhap giay k: "))
print("gio,phut,giay: ",hh,":",mm,":",ss,)
print(hh,"gio sang giay",hh*3600)
print(mm,"phut sang giay",mm*60)
print("gio,phut,giay: ",hh,":",mm,":",ss,"doi sang giay =",hh*3600+mm*60+ss)
nt = hh*3600+mm*60+ss+k
print("gio,phut,giay: ",hh,":",mm,":",ss,"doi sang giay them + k =",time.strftime('%H:%M:%S', time.gmtime(nt)))
