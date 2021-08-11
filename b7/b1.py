file = open('data71.txt','w',encoding='utf-8')

for i in range(1,11):
    file.write('\n'+str(i))
file.close()

file = open('data71.txt','r+',encoding='utf-8')
result = 0
for i in file:
    result = sum(map(int, file))
    file.write('\ntong so: '+str(result))
file.close()

file = open('data71.txt','r',encoding='utf-8')
print(file.read())
file.close()