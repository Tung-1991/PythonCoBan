import nltk
#nltk.download('popular')
from urllib import request
from bs4 import BeautifulSoup
#lay van ban tu url
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
#in ra các từ trong văn bản
raw = response.read().decode('utf8')
print(type(raw))#kiểu văn bản
print(len(raw))#đếm tất cả trong văn bản
print(raw[1:74])#in các chỉ số từ 1 tới 73
#tách các từ ra dạng list
tokens = nltk.word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[1:10])

url = 'https://sites.google.com/site/nmhien/thtt'
html = request.urlopen(url).read().decode('utf8')
print(html[:60])
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = nltk.word_tokenize(raw)
print(tokens[:10])

#tạo một văn bản
raw = 'DENNIS: Listen, strange women lying in ponds ' \
      'distributing swords is no basis for a system of government. ' \
      'Supreme executive power derives from a mandate from the masses, ' \
      'not from some farcical aquatic ceremony.'
tokens = nltk.word_tokenize(raw)
porter = nltk.PorterStemmer()#khai bảo tách gốc porter
ds = [porter.stem(t) for t in tokens]#chuẩn hóa theo porter
print(ds)