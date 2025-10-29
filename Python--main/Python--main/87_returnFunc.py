#Q87. Demonstrate early return in a function

def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None

nums = [1, 3, 5, 8, 9]
first_even = find_first_even(nums)
print(first_even)

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")