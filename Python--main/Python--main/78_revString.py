#Q78. reverse a string without a predefined function

def stringReverse(s):
    rs=" "
    for char in s:
        rs=char+rs
    print(rs)
stringReverse(input("Enter a string: "))

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")