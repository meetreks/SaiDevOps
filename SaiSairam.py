#TO print Fibo Series to 10!!!
y = 0
for i in range(10):
    x = i
    if(x == 0):
        y = x+ y
        print(y)
    elif(x == 1):
        y = x+ y
        print(y)
    elif(x == 2):
        print(1)
        prev = 1
        prevt = 1
    else:
        kukhi = prevt + prev
        print(kukhi)
        prevt = prev
        prev = kukhi









