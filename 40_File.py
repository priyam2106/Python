
# Reading a file
f=open("pc.txt","r")

content = f.read()
print(content)
f.close()


# Writing a file
f = open("Priyam.txt","w")

string='''Hello guys
byy guys'''
f.write(string)


# Append to an existing file
f2=open("pc.txt","a")
string2=''' Go ahead 
stay safe'''

f2.write(string2)
f2.close()


# line by line

f=open("pc.txt","r")
for line in f:
    print(line)

f.close()


with open("pc.txt","r") as f:
    content=f.read()
    print(content)