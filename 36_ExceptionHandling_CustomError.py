# while True:
#     try:
#         a = int(input("Enter number 1: \n"))
#         b = int(input("Enter number 2: \n"))
#         # print(f"The sum is {a+b}")
#         print(f"Divide{a/b}")

#     except ValueError:
#         print("Please dont perform bad calculation")

#     except ZeroDivisionError:
#         print("Hey don't divide by 0")

#     except Exception as e:
#         print("Some Error Occured!", e)


# a = int(input("Enter number 1: "))
# b= int(input("Enter number 2: "))

# if b==0:
#     raise ValueError("Please dont divide by 0")
# print(f"The Division is {a/b}")


# try:
#     a=345/10

# except Exception as e:
#     print(e)

# else:
#     print("Hey I am Good")

a = int(input("Enter number 1: "))
b= int(input("Enter number 2: "))

try:
    c=a/b
    print(c)

except Exception as e:
    print(e)

finally:
    print("This is always executed")