n = int(input('nhap n: '))
snt = True
if n <2:
    snt= False
else:
    i=2
    while(i<n-1):
        if(n%i==0):
            snt=False
            break
        i = i+1
for i in range(n):
    if snt == True:
        print(i,"la snt")
    else:
        print(i,"khong la snt")