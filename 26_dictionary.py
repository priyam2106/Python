marks ={"priyam":100,"Akash":45,"Panoti":-100}
print(marks["Panoti"])

marks["Akash"]=54
print(marks)

print(marks.keys())
print(marks.values())
marks.pop("Panoti")
print(marks)
marks.clear()
print(marks)


#  dictionary comprehension

table_of_5 ={i: 5*i for i in range (1,11)}
print(table_of_5)