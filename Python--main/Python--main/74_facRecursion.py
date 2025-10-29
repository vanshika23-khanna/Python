#Q74. Factorial of a number simple using recursion

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

# Taking input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")