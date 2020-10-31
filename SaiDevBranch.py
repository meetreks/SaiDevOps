for i in range(1,10):
    if(i == 1):
        print(i)
    elif(i ==2 ):
        print(2)
        prev = 2
    else:
        j = i * prev
        print(j)
        prev = j
