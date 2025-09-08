try:
   number = int(input("Enter a number: "))
   result = 10 / number
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"The result is {result}.")

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
