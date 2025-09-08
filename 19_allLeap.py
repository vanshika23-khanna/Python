count = 0
for year in range(1, 2025):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end="  ")  
        count += 1

print("\n\nTotal leap years till 2025:", count)

print("This program is written and executed by Vanshika Khanna, 0231BCA033")
