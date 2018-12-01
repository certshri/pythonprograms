for i in range (0, 5):
    num = 1
    for j in range (0, i+1):
      print(num, end=" ")
      if num == 1:
         num = 0
      else:
         num = 1
    print("")