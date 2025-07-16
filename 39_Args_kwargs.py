# def sum(*args):
#     # args will be a tuple of all the values passed to sum
#     print(args)
#     total = 0
#     for item in args:
#         total +=item
#     return total

# print(sum(4,6,342,8))

# def marks(**kwargs):
#     # kwargs is a dictionary with all the key value pairs which were passed to marks
#     for item in kwargs.keys():
#         print(f"The marks of {item} is {kwargs[item]}")

# marks(shubham=34,vikrant=54,jack=69,Marie=90)


def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,3,7,jack = 56,jill=78)
