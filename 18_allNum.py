start = int(input("Enter start: "))
end = int(input("Enter end: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return num > 0 and sum(i for i in range(1, num) if num % i == 0) == num

def is_armstrong(num):
    p = len(str(num))
    return sum(int(d)**p for d in str(num)) == num

print("Prime numbers:", [n for n in range(start, end+1) if is_prime(n)])
print("Perfect numbers:", [n for n in range(start, end+1) if is_perfect(n)])
print("Armstrong numbers:", [n for n in range(start, end+1) if is_armstrong(n)])

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
