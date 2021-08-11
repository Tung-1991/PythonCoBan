file = open('data72.txt','a',encoding='utf-8')
hoten = input("hoten: ")
tuoi = input("tuoi: ")
file.write("\t".join([hoten, tuoi])+"\n")
file.close()

file = open('data72.txt','r',encoding='utf-8')
for sv in file.readlines():
    print(sv)
file.close()