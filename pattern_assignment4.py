for i in range (0, 5):
    if i%2==0:
        num = 0
    else:
        num = 1
    for j in range (0, i+1):
        print(num, end=" ")
        if num == 0:
            num = 1
        else:
            num = 0
    print("")