num = 1
for i in range (0, 5):
    for j in range (0, 5):
        print("{:02d}".format(num), end= " ")
        num = num + 1
    print(" ")