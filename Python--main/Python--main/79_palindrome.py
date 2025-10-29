#Q79. Check whether the string is Palindrome

def is_palindrome(s):
    s=s.lower()
    left=0
    right=len(s)-1
    while left<right:
        if s[left]==s[right]:
            return False
        left+=1
        right-=1
    return True

text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")