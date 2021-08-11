print("hello world")
def avg(vals):
    sum = 0
    for v in vals:
        sum = sum + v
    return sum / len(vals)

print(avg([4,6,2]))