year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
