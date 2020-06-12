def fibonacci(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))    #fibonacci sequence equation is f(n) = f(n-1) + f(n-2)
x = int(input("Enter any number."))
print(fibonacci(x))
