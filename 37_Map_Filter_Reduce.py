# Map

# numbers=[1,2,3,4]

# def square(x):
#     return x*x


# new = list(map(lambda x:x*x,numbers))
# print(new)

# Filter

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    

# a = [1,3,4,5,34,54,32,555,3,9,8,7,0]

# new = list(filter(is_greater_than_9,a))
# print(new)


# Reduce
from functools import reduce

a =[1,2,3,4,5,6]
''' [3,3,4,5,6 ]
    [6,4,5,6]
    [10,5,6]
    [15,6]
    [21]'''

def sum(a,b):
    return a+b

c= reduce(sum, a)
print(c)
