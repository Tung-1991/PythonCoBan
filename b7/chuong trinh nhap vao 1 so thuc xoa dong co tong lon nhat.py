def maxelement(matran):
    max1 = []
    l1 = []
    l2 = []
    for i in range(len(matran)):
        tong = 0
        for j in range(len(matran[0])):
            tong = tong + matran[i][j]
            for k in range(0,1):
                l1.append(matran[j][i])
        if len(l1)==4:
            print(l1)
        print("tong cac hang",tong)
        max1.append(tong)
    print("tong lon nhat: ",max(max1))

matran = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]
maxelement(matran)
a,b,c,d = matran
print(a,b,c,d)
if sum(c) > sum(a) and sum(c)>sum(b) and sum(c) > sum(d):
    matran.remove(c)
print(matran)

