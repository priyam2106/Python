name="Priyam go"  # Strings are Immutable

# name[0] ="E" # you cannot do this

# a = len(name)

# print(a)

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())


# text ="  hello world  "

# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# print(text.find("world"))
# print(text.replace("world","universe"))

text ="Apples,Banana,Pineapples"

print(text.split(","))
print(",".join(['Apples','Bananas','Pineapples']))
print(text)


text ="Python123"

print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isspace())