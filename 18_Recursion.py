def fib(n):
    if (n==0 or n==1):
        return n
    
    return fib(n-2)+fib(n-1)

print(fib(6))


def fact(n):
    if (n==0):
        return 1
    
    return  n*fact(n-1)

print(fact(5))
    