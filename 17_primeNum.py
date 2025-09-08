n = int(input("Enter number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime number")
else:
    print("Not prime")

print("\n\nThis program is written and executed by Vanshika Khanna, 0231BCA033")
