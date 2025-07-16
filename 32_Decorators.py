#Decorators is sthe function that takes a function , it creates a new function inside its body (wrapper). Then returns the new function

def decorator(func):
    def wrapper():
        print("I am about to print hello")
        func()
        print("I have executed this function")
    return wrapper



@decorator
def say_hello():
    print("Hello")

say_hello()
# f=decorator(say_hello)
# f()

#Decorators with Arguments



def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(b):
    print(f"Hello {b}")

say_hello("Priyam")
