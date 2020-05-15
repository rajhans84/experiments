def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    return fact
#answer = factorial(5)


def stars1(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("\n")
# stars1(6)        

def stars2(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print("\n")

def stars3(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(" ", end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print("\n")

def stars4(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print("\n")

def fib(n):
    a = 1
    b = 1
    while a<=n:
        print(a)
        c = a + b
        a = b
        b = c

def star5(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print("\n")

def arrow(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print("\n")
    for k in range(n-1, 0, -1):
        for l in range(k):
            print("*", end=" ")
        print("\n")