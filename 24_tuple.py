a=(3,4,5,6,7) # immutable

print(a)
print(a[2])

# a[2]=7 # it will not change

b = (6,)# if we have to create a tuple of single element we have to put comma after the element
tu=(6,7,8)
a,b,c = tu
print(a,b,c)


t=(3,3,23,4,5,7,3)

print(t.count(3))
print(t.index(3))