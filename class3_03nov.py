""" Dictionary"""
#blank_dict = dict()
#blank_dict['name'] = 'swami'
#print(blank_dict)
# """ set and tuple """
# """write a code to find maximum no from 5 values"""
# no_1 = 7
# no_2 = 5
# no_3 = 100
# no_4 = 23
# no_5 = 102
# if no_1 > no_2:
#     print ('Max no is',no_1)
# Else no_3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))