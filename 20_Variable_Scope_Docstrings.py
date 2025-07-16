def sum (a,b):
    c=a+b
    return c
z=8
# print(sum(4,5))

def mul(a,b):
    '''This will sum two numbers'''
    global z
    z=5
    d = a*b*z
    print(d)

mul(2,3)
print(z)

print(mul.__doc__)



