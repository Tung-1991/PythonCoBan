l = [2,7,11,15]
for i in l:
    for j in l:
        if i + j == 9:
            print("true")
            for position, k in enumerate(l):
                if i == k:
                    print([position])
