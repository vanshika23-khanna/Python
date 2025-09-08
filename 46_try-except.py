try:
   number = int(input("Enter a number: "))
   result = 10 / number
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input, Enter a valid number.")

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
