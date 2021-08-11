
import nltk

def doc(path):
  o = open(r'C:\Users\tungp\PycharmProjects\pythonProject\THTT\TH2\\'+path+'.txt','r',encoding='utf8')
  r = o.read()
  tokens = nltk.word_tokenize(r)
  return tokens

Name = 'An Giang, Bac Ninh, Binh Thuan, Cao Bang, Ha Noi, Hai Phong, Lai Chau, Lang Son, Thai Nguyen, TP HCM'
Name = Name.split(', ')
L = []
for i in Name:
  L.append(doc(i))
print(L)

dem = 1
A = []
for i in L:
  dic = {}
  for j in i:
    j = j.lower()
    dic[j] = dem
    if (dic not in A):
      A.append(dic)
  dem = dem + 1
print(A)
for i in A:
  print(i)

a = str(input("Nhập từ cần tìm: ")).lower()

DS = []
for i in A:
  for j in i:
    if (a == j):
      DS.append(i[j])
print("Danh sách ID các bài hát có chứa từ cần tìm là:", DS)

b = int(input("Nhập ID bài hát: "))
print("Tên bài hát là:", Name[b])
print("Lyric: \n")

print(open(r'C:\Users\tungp\PycharmProjects\pythonProject\THTT\TH2\\'+ Name[b] + '.txt','r',encoding='utf8').read())