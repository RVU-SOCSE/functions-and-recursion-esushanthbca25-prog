#E Sushanth
#1RUA25BCA0030


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


num = int(input("Enter number of terms: "))

print("Fibonacci term =", fib(num))
