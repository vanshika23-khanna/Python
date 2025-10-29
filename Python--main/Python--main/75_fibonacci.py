# Fibonacci using simple function (iteration)
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # new line


# Fibonacci using recursion
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# Main program
n = int(input("Enter number of terms: "))

print("Fibonacci series using simple function:")
fibonacci_iter(n)

print("Fibonacci series using recursion:")
for i in range(n):
    print(fibonacci_rec(i), end=" ")

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")