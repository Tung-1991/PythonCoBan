from ssl import DER_cert_to_PEM_cert
import nltk
ds={'An Giang.txt':1,'Bac Ninh.txt':21,'Binh Thuan.txt':33,'Cao Bang.txt':3,'Ha Noi.txt':5,'Hai Phong.txt':6,'Lang Son.txt':7,'Lai Chau.txt':8,'Thai Nguyen.txt':9,'TP HCM.txt':10,}
ds2={} #danh sach sau khi xu ly
list_key=[]
for i in ds:
    dict1={}
    stt = ds[i]
    f = open(r'C:\Users\tungp\PycharmProjects\pythonProject\THTT\TH2\\'+i)
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    porter = nltk.PorterStemmer()
    # tach
    dict1 =[porter.stem(t) for t in tokens]
    #gan so van ban
    dict2 = i;
    dict2 = {}
    for i in dict1:
        dict2[i]=stt
    # chuyen vao ds2
    ds2[i]=dict2
#ham lay key
def getList(ds):
    return ds.keys()
# ds2 sau khi doi key
ds2=dict(zip(getList(ds), list(ds2.values())))
print(ds2)
print("Nhap tu muon tim kiem : ")
w = input();

vitri=[]
for id,info in ds2.items():
    for key in info:
        if w == key:
            vitri.append(ds2[id][key])

# print(vitri)
search=[]
for key,val in ds.items():
    for i in vitri:
        if i == ds[key]:
            search.append(key)

if len(search)!=0:
    print("tu "+"'"+w+"'"+" xuat hien trong van ban :")
    for i in search:
        print("-"+i)
else:
    print("khong tim thay"+"'"+w+"'")