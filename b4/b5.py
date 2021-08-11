#Trăm Trâu ăn cỏ
#Trâu đứng ăn năm
#Trâu nằm ăn ba
#Ba Trâu già ăn một
#Hỏi số trâu mỗi loại
for i in range(100):
    for j in range(100):
        for k in range(100):
            if (5*i + 3*j + k/3 == 100 and k%3==0 and i + j +k == 100 and i>0):
                print("Trau Dung: ",i)
                print("Trau Nam: ", j)
                print("Trau Gia: ", k)