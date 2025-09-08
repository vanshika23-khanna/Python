count = 0  
print("Perfect Numbers from 1 to 2025:")

for num in range(1, 2026):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(num, end=" ")
        count += 1

print("\nTotal Perfect Numbers:", count)

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
