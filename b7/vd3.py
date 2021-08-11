import pandas as pd
import os
def nhapsv():
    file = open("svchung.txt",'a',encoding='utf-8')
    while True:
        maSV = input("Ma SV: ")
        if maSV =="":
            break
        tenSV = input("Ten SV: ")
        lop = str(input("lop: "))
        QueQuan = input("Que quan: ")
        file.write('\t'.join([maSV,tenSV,lop,QueQuan])+'\n')
    file.close()
def docdssvtufile(file):
    SV = pd.read_csv(file, sep='\t', header=None, names=['Ma_SV', 'Ten_SV', 'lop_SV', 'QueQuanSV'])
    return SV
def hienthidssvlopSV(lop,DSSV):
    DSSVten = DSSV.query("lop_SV == @lop")
    sosv = DSSVten.shape[0]
    if sosv > 0:
        print("co: ",sosv,"sinh vien co lop",lop)
        print(DSSVten)
    else:
        print("ko co sinh vien nao co lop: ",lop)
def hienthidssvtenSV(tenSV,DSSV):
    DSSVten = DSSV.query("Ten_SV == @tenSV")
    sosv = DSSVten.shape[0]
    if sosv > 0:
        print("co: ",sosv,"sinh vien co ten",tenSV)
        print(DSSVten)
    else:
        print("ko co sinh vien nao co ten: ",tenSV)
def ghidssvvaofile(dssv):
    DSlop = dssv['lop_SV'].unique()
    for lop in DSlop:
        sv_lop = dssv.query("lop_SV == @lop")
        sv_lop.to_csv(lop+'.txt',index=None,encoding='utf-8',sep='\t')
file="svchung.txt"
nhapsv()
SV = docdssvtufile(file)
hienthidssvlopSV('59',SV)
hienthidssvtenSV('tung',SV)
ghidssvvaofile(SV)