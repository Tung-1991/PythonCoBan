n= int(input("nhap n: "))

for num in range(n + 1):
    if num > 1:
        for i in range(2, num-1):
            if (num % i) == 0:
                break
        else:
            print(num)