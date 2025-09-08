try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result is:", result)
finally:
    print("Program finished")

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
